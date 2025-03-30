import http
import json

from django.contrib.auth import authenticate

import jwt
import requests
from django.conf import settings
from django.core.exceptions import BadRequest

AUTH0_DOMAIN = settings.AUTH0_DOMAIN
AUTH0_API_ID = settings.AUTH0_API_ID

AUTH0_MTM_CLIENT_SECRET = settings.AUTH0_MTM_CLIENT_SECRET
AUTH0_MTM_CLIENT_ID=settings.AUTH0_MTM_CLIENT_ID

AUTH0_LOGIN_DOMAIN = settings.AUTH0_LOGIN_DOMAIN
AUTH0_APP_CLIENT_SECRET = settings.AUTH0_APP_CLIENT_SECRET
AUTH0_APP_CLIENT_ID = settings.AUTH0_APP_CLIENT_ID


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username

def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format(AUTH0_DOMAIN)).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format(AUTH0_DOMAIN)
    return jwt.decode(token, public_key, audience=AUTH0_API_ID, issuer=issuer, algorithms=['RS256'])


def get_machine_to_machine_token():
    conn = http.client.HTTPSConnection("dev-d8bmthb8ix428twj.us.auth0.com")

    payload ={
        "client_id":AUTH0_MTM_CLIENT_ID,
        "client_secret":AUTH0_MTM_CLIENT_SECRET,
        "audience":AUTH0_API_ID,
        "grant_type":"client_credentials"
    }


    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", json.dumps(payload), headers)

    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

def get_user_token(username,password):
    response = requests.post(
        url="https://{}/oauth/token".format(AUTH0_LOGIN_DOMAIN),
        data={
            "grant_type":"password",
            "username":username,
            "password":password,
            "client_id":AUTH0_APP_CLIENT_ID,
            "client_secret":AUTH0_APP_CLIENT_SECRET,
            "audience":AUTH0_API_ID,
            "scope":"openid profile email"
        },
        headers={'content-type': "application/x-www-form-urlencoded"}
    )
    if response.status_code != 200:
        raise BadRequest('Token request failed.')

    return response.json()
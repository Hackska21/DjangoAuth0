from django.db.models import Count
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth0_auth import get_machine_to_machine_token, get_user_token
from apps.example.models import ExampleModel
from apps.example.serializers import ExampleAggregationSerializer, ExampleModelSerializer, \
    LoginSerializer


class ProtectedView(CreateAPIView):
    serializer_class = ExampleModelSerializer


class PublicView(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ExampleAggregationSerializer

    def list(self, request, *args, **kwargs):
        res = ExampleModel.objects.aggregate(
            count=Count('pk')
        )
        serializer = self.get_serializer(res)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60 * 2))
    @action(detail=False, methods=["get"], name="Get token")
    def get_token(self, request):
        res = get_machine_to_machine_token()
        return Response(res)

    @action(detail=False, methods=["post"], name="Get user token")
    def get_user_token(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = get_user_token(**serializer.validated_data)
        return Response(res)

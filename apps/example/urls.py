from django.urls import path, include
from rest_framework import routers

from apps.example.views import ProtectedView, PublicView

router = routers.SimpleRouter()
router.register(r'', PublicView,basename='public')

urlpatterns = [
    path('private/', ProtectedView.as_view()),
    path('public/', include(router.urls))
]
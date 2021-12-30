from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from core.serializers import WriteOnlyUserSerializer, ReadOnlyUserSerializer


class UserModelViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadOnlyUserSerializer
        return WriteOnlyUserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser is True:
            return User.objects.all()
        return User.objects.filter(username=self.request.user)

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from intobi_app.core.permissions import IsSuperUser
from intobi_app.vote.models import Vote
from intobi_app.vote.services import prepare_data
from intobi_app.vote.verioning import VoteVersioning

from .serializers import VoteNewSerializer, VoteOldSerializer, VoteSerializer

User = get_user_model()


class VoteViewSet(DestroyModelMixin, ListModelMixin, GenericViewSet):
    versioning_class = VoteVersioning
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsSuperUser, IsAdminUser)

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Vote.objects.all()
        else:
            queryset = (
                super().get_queryset().filter(restaurant=self.request.user.restaurant)
            )
        return queryset


class VotingView(CreateModelMixin, GenericViewSet):
    versioning_class = VoteVersioning
    queryset = Vote.objects.all()

    def get_serializer(self, instance=None, data=None, many=False, partial=False):
        if self.request.version == "1.0":
            self.serializer_class = VoteOldSerializer
            return super().get_serializer(instance=instance, data=data, partial=partial)
        elif self.request.version == "1.1":
            self.serializer_class = VoteNewSerializer
            return super().get_serializer(
                instance=instance, data=data, many=True, partial=partial
            )

    def create(self, request, *args, **kwargs):
        if len(request.data) == 3:
            data = prepare_data(data=request.data, user=request.user.pk)
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

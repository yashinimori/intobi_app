from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from intobi_app.core.permissions import IsSuperUser
from intobi_app.core.services import get_top_menu

from .serializers import Menu, MenuSerializer, Restaurant, RestaurantSerializer

User = get_user_model()


class RestaurantViewSet(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
    permission_classes = (IsSuperUser,)


class MenuViewSet(ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Menu.objects.all()
        else:
            queryset = (
                super().get_queryset().filter(restaurant=self.request.user.restaurant)
            )
        return queryset

    def create(self, request, *args, **kwargs):
        if request.user.is_staff:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CurrentMenuView(ListModelMixin, GenericViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects

    def get_queryset(self):
        menus = Menu.objects.filter(
            restaurant=self.request.user.restaurant
        ).values_list("pk", flat=True)
        return Menu.objects.filter(pk=get_top_menu(menus))

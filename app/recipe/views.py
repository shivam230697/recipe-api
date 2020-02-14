from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from app.core.models import Tag, Ingredient
from app.recipe import serializers
from rest_framework import viewsets, mixins


# Create your views here.

class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

    def get_queryset(self):
        """

        :return:
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def Perform_create(self):
        serializers.save(user=self.request.user)


class IngredientsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """

    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredeintSerializer

    def get_queryset(self):
        """

        :return:
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')


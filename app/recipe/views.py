from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from app.core.models import Tag, Ingredient
from app.recipe import serializers
from rest_framework import viewsets, mixins


# Create your views here.

class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """

        :return:
        """
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def Perform_create(self):
        serializers.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientsViewSet(BaseRecipeAttrViewSet):
    """

    """
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredeintSerializer

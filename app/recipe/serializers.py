from rest_framework import serializers
from app.core.models import Tag
from app.core.models import Ingredient


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = {'tag', 'name'}
        read_only_fields = {'id', }


class IngredeintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = {'tag', 'name'}
        ead_only_fields = {'id', }

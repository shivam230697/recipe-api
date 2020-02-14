from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """serializer for user object"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        """extra kwargs allows you to do is just set some extra restrictions 
            or arguments for the fields that we reference 
            in our fields variable here."""
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validate_data):
        """create a new user with encrypted password and return it."""
        print(validate_data)
        return get_user_model().obj.create_user(**validate_data)

    def update(self, instance,  validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _("unable to authenticate ")
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

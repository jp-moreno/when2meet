from rest_framework import serializers
from .models import User

class UserSerialiazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "pic"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    # https://stackoverflow.com/questions/27586095/why-isnt-my-django-user-models-password-hashed hasing password properly
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
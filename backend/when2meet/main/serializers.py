from rest_framework import serializers
from .models import User, Event, TimeRange, Available

class UserSerialiazer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "pic"]
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event

class TimeRangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeRange

class AvailableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avialable

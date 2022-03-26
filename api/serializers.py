from rest_framework import serializers
from api.models import CarList, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarList
        fields = "__all__"        
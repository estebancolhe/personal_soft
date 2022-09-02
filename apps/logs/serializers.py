from rest_framework import serializers
from apps.logs.models import Log, ActionType


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


class ActionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'


class logLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = 'users','trainingPath','actionType','ipUser','value','url'
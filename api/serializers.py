from rest_framework import serializers
from .models import GPTBot, Scenario, Step

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'

class GPTBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPTBot
        fields = '__all__'
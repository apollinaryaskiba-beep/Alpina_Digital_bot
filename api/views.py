import openai
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import GPTBot, Scenario, Step
from .serializers import GPTBotSerializer, ScenarioSerializer, StepSerializer

# Вставьте ваш ключ сюда, если он появится (sk-...)
openai.api_key = "YOUR_FREE_TRIAL_KEY"


class GPTBotViewSet(viewsets.ModelViewSet):
    queryset = GPTBot.objects.all()
    serializer_class = GPTBotSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer

    @action(detail=True, methods=['get'])
    def steps(self, request, pk=None):
        scenario = self.get_object()
        serializer = StepSerializer(scenario.steps.all(), many=True)
        return Response(serializer.data)


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    @action(detail=True, methods=['post'])
    def run(self, request, pk=None):
        step = self.get_object()
        user_input = request.data.get('input', '')

        # Интегрирация с GPT API
        try:
            # Если ключ не задан, имитируем ответ для теста
            if openai.api_key == "YOUR_FREE_TRIAL_KEY":
                mock_response = f"[Имитация GPT]: Обработка вашего вопроса '{user_input}' по сценарию '{step.scenario.name}'. Использован промпт: {step.config.get('prompt')}"
                return Response({"result": mock_response, "status": "demo_mode"})

            # Если ключ есть, вызываем реальный OpenAI
            response = openai.ChatCompletion.create(
                model=step.config.get('model', 'gpt-3.5-turbo'),
                messages=[
                    {"role": "system", "content": step.config.get('prompt', 'Ты помощник Альпины')},
                    {"role": "user", "content": user_input}
                ]
            )
            return Response({"result": response.choices.message.content})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
from django.contrib import admin
from .models import GPTBot, Scenario, Step

# Регистрация моделей в админке
admin.site.register(GPTBot)
admin.site.register(Scenario)
admin.site.register(Step)
from django.db import models


class GPTBot(models.Model):
    """Модель бота Alpina.GPT"""
    name = models.CharField(max_length=100, verbose_name="Имя бота")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Бот"
        verbose_name_plural = "Боты"

    def __str__(self):
        return self.name


class Scenario(models.Model):
    """Сценарий взаимодействия бота с пользователем"""
    bot = models.ForeignKey(GPTBot, on_delete=models.CASCADE, related_name='scenarios', verbose_name="Бот")
    name = models.CharField(max_length=100, verbose_name="Название сценария")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Сценарий"
        verbose_name_plural = "Сценарии"

    def __str__(self):
        return f"{self.name} ({self.bot.name})"


class Step(models.Model):
    """Отдельный шаг сценария с настройками для GPT API"""
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, related_name='steps', verbose_name="Сценарий")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок шага")

    # Формат JSON для хранения состояний и промптов
    config = models.JSONField(
        default=dict,
        verbose_name="Конфигурация GPT (JSON)",
    )

    class Meta:
        ordering = ['order']
        verbose_name = "Шаг сценария"
        verbose_name_plural = "Шаги сценария"

    def __str__(self):
        return f"Шаг {self.order} -> {self.scenario.name}"
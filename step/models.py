from django.db import models
from django.utils import timezone


class Step(models.Model):
    user = models.ForeignKey("account.User", verbose_name="Пользователь", on_delete=models.CASCADE, related_name="step")
    count = models.IntegerField("Количество", default=0)

    date = models.DateField("Дата", default=timezone.now)

    class Meta:
        verbose_name = "Шагомер"
        verbose_name_plural = "Шаги"

    def __str__(self):
        return f"{self.id}| {self.user}: {self.count}"

    @property
    def status(self):
        return "Вы достигли цели!" if self.count >= self.user.step_target else "Пора прогуляться."

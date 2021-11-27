from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

from fitness.models import UserFitness


class User(AbstractUser, UserManager):
    image = models.ImageField(_("Аватар пользователя"), blank=True, null=True, upload_to="user/image")
    balance = models.FloatField(_("Баланс"), default=0.00)
    money_limit = models.FloatField(_("Денежный лимит"), default=30000.00)
    step_target = models.IntegerField(_("Цель по шагам"), default=10000)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username

    @property
    def current_exercise(self):
        return self.fitness.filter(is_current=True).first()

    @current_exercise.setter
    def current_exercise(self, instance: UserFitness):
        """ Обновление активного упражнения """
        if isinstance(instance, UserFitness):
            user_fitness = self.fitness.all()
            for fitness in user_fitness:
                if fitness.id == instance.id:
                    setattr(fitness, "is_current", True)
                else:
                    setattr(fitness, "is_current", False)
            UserFitness.objects.bulk_update([*user_fitness], ['is_current'])
            print(1, instance.is_current)

    def get_all_exercises(self):
        return self.fitness.all

    def update_balance(self, money: float) -> float:
        self.balance += money
        self.save()
        return self.balance

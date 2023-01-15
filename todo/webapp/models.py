from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    deadline = models.DateTimeField(verbose_name="Срок выполнения")
    performed = models.BooleanField(default=False, verbose_name="Выполнено/Не выполнено")

    def __str__(self):
        return f"{self.id}. {self.title}: {self.description}.{self.performed}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
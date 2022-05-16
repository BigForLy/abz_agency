from django.db import models


class PositionAtWork(models.Model):

    title = models.CharField(
        verbose_name='Название', 
        max_length=128,
        unique=True
    )

    def __str__(self) -> str:
        return f'{self.title}'
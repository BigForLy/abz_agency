from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
from django.conf import settings


def upload_to(instance, filename):
    return '/'.join( ['staff', str(instance.pk), filename] )


class Staff(MPTTModel):

    image = models.ImageField(
        upload_to=upload_to,
        max_length=254,
        null=True
    )

    first_name = models.CharField(
        verbose_name='Имя', 
        max_length=128
    ) 

    last_name = models.CharField(
        verbose_name='Фамилия', 
        max_length=128
    ) 

    patronymic = models.CharField(
        verbose_name='Отчество', 
        max_length=128
    )
    
    position_at_work = models.ForeignKey(
        to='position_at_work.PositionAtWork',
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name='Должность'
    )

    employment_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата приема на работу'
    )

    wage = models.PositiveIntegerField(
        'Заработная плата'
    )

    parent = TreeForeignKey(
        to='Staff', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name='subordinate',
        verbose_name='Начальник'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name[0]}. {self.patronymic[0]}.'

    class MPTTMeta:
        db_table = 'staff'

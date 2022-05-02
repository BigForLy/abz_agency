from rest_framework import serializers

from staff.models import (Staff, PositionAtWork)


class StaffSerializer(serializers.ModelSerializer):

    # position_at_work = serializers.StringRelatedField()

    class Meta:
        model = Staff
        fields = ['id', 'first_name', 'last_name', 'patronymic', 'position_at_work', 'employment_date', 'wage', 'parent']


class PositionAtWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionAtWork
        fields = '__all__'
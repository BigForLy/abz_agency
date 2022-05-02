import functools
import time
from django.db import connection, reset_queries
from django.http import Http404
from rest_framework import views
from staff import serializers

from staff.models import Staff, PositionAtWork
from staff.serializers import (StaffSerializer, PositionAtWorkSerializer)
from rest_framework.response import Response
from rest_framework import generics, status, mixins


def query_debugger(func):

    # @functools.wraps(func)
    def inner_func(*args, **kwargs):

        reset_queries()
        
        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


class StaffView(generics.ListCreateAPIView):

    serializer_class = StaffSerializer

    def get_queryset(self):
        return Staff.objects.all().get_cached_trees()

    @query_debugger
    def get(self, request):
        qyeryset = self.get_queryset()

        data = []
        for item in qyeryset:
            data.append(self.recursive_subordinate(item))

        return Response(data)

    def recursive_subordinate(self, item):
        result = StaffSerializer(item).data
        subordinate = [self.recursive_subordinate(c) for c in item.get_children()]
        if subordinate:
            result["Подчиненный"] = subordinate
        return result


class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class CompanyStructure(views.APIView):
    pass


class PositionAtWorkView(generics.ListCreateAPIView):
    
    queryset = PositionAtWork.objects.all()
    serializer_class = PositionAtWorkSerializer


class PositionAtWorkDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = PositionAtWork.objects.all()
    serializer_class = PositionAtWorkSerializer

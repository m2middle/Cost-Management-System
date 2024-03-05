from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema_view, extend_schema

from .serializers import DepartmentSerializer
from .models import Department
from employees.permissions import IsManager

# Create your views here.

@extend_schema_view(
    post=extend_schema(
        description="Route to create Department. Route only for managers",
        summary="Create a Department",
        tags=["Departments"],
    ),
    get=extend_schema(
        description="Route to list all Departments. Route only for managers",
        summary="List all Departments",
        tags=["Departments"],
    ),
)
class DepartmentView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

@extend_schema_view(
    get=extend_schema(
        description="Route to list Department by id. Route only for managers",
        summary="List Department by id",
        tags=["Departments"],
    ),
    patch=extend_schema(
        description="Route to update a Department. Route only for managers",
        summary="Update Department",
        tags=["Departments"],
    ),
    delete=extend_schema(
        description="Route to delete a Department.Route only for managers",
        summary="Delete Department",
        tags=["Departments"],
    ),
    put=extend_schema(exclude=True),
)
class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
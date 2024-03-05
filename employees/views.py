from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.serializers import ModelSerializer
from .models import Employee
from .permissions import IsManager, isAdminGet
from .models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

@extend_schema_view(
    post=extend_schema(
        description="Route to create Employees",
        summary="Create Employees",
        tags=["Employees"],
    ),
    get=extend_schema(
        description="Route to list all Employees. Route only for managers",
        summary="List all Employees",
        tags=["Employees"],
    ),
)
class EmployeeView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManager]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@extend_schema_view(
    get=extend_schema(
        description="Route to list Employee by id. Route only for managers",
        summary="List Employee by id",
        tags=["Employees"],
    ),
    patch=extend_schema(
        description="Route to update Employee by id. Route only for managers",
        summary="Update Employee",
        tags=["Employees"],
    ),
    put=extend_schema(
        description="Route to replace Employee by id. Route only for managers",
        summary="Replace Employee",
        tags=["Employees"],
    ),
)
class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [isAdminGet]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
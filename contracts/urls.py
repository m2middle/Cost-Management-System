from django.urls import path
from .views import ContractView, ContractDetailView

urlpatterns = [
    path('', ContractView.as_view(), name='contract-list-create'),  
    path('<int:pk>/', ContractDetailView.as_view(), name='contract-detail'),
]
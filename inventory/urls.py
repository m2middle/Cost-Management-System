from django.urls import path
from .views import InventoryListCreate, InventoryRetrieveUpdateDestroy, InventoryHistoryListCreate, InventoryHistoryRetrieveUpdateDestroy

urlpatterns = [
    path('', InventoryListCreate.as_view(), name='inventory_list_create'),
    path('<int:pk>/', InventoryRetrieveUpdateDestroy.as_view(), name='inventory_retrieve_update_destroy'),
    path('', InventoryHistoryListCreate.as_view(), name='inventory_history_list_create'),
    path('<int:pk>/', InventoryHistoryRetrieveUpdateDestroy.as_view(), name='inventory_history_retrieve_update_destroy'),
]
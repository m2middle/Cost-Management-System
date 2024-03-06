from django.urls import path
from .views import CategoryView, CategoryDetailView

urlpatterns = [
    path('', CategoryView.as_view(), name='category_list_create'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category_retrieve_update_destroy'),
]
from django.urls import path
from . import views


urlpatterns = [
    path("suppliers/", views.SupplierView.as_view()),
    path("suppliers/<int:pk>/", views.SupplierDetailView.as_view())
]
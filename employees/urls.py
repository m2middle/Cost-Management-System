from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("", views.EmployeeView.as_view()),
    path("<int:pk>/", views.EmployeeDetailView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
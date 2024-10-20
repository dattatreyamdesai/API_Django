from django.urls import path
from countries import views

urlpatterns = [
    path('countries/', views.countries_list),  # Add trailing slashes
    path('countries/<int:pk>/', views.countries_detail),  # Add trailing slashes
]

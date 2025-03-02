from django.urls import path
from . import views

urlpatterns = [
    # Authentication Endpoints
    path('auth/login/', views.login_view, name='login'),
    path('auth/signup/', views.signup_view, name='signup'),

    # Disease CRUD Endpoints
    path('diseases/', views.disease_list, name='disease-list'),          # List and Create
    path('diseases/<int:pk>/', views.disease_detail, name='disease-detail'),  # Retrieve, Update, Delete
]

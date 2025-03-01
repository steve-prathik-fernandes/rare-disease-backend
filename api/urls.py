from django.urls import path

from . import views

urlpatterns = [
    # Authentication Endpoints
    path('auth/login/', views.login_view, name='login'),
    path('auth/signup/', views.signup_view, name='signup'),

    # Disease Search Endpoint
    path('diseases/', views.DiseaseListView.as_view(), name='disease-list'),
    path('diseases/search/', views.search_diseases, name='search-diseases'),  # ✅ Search API
]

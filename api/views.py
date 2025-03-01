from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView

# 🛠 Authentication Views
@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(username=email, password=password)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

# 🛠 Disease API Views
class DiseaseListView(APIView):
    def get(self, request):
        sample_data = [
            {"name": "Disease 1", "description": "Description of Disease 1"},
            {"name": "Disease 2", "description": "Description of Disease 2"},
            {"name": "Disease 3", "description": "Description of Disease 3"}
        ]
        return JsonResponse(sample_data, safe=False)

@api_view(['GET'])
def search_diseases(request):
    query = request.GET.get('q', '')
    if query:
        # Example filtered data (in real app, use database filter)
        sample_data = [
            {"name": "Disease 1", "description": "Description of Disease 1"},
            {"name": "Disease 2", "description": "Description of Disease 2"},
            {"name": "Disease 3", "description": "Description of Disease 3"}
        ]
        filtered = [d for d in sample_data if query.lower() in d['name'].lower()]
        return JsonResponse(filtered, safe=False)
    else:
        return JsonResponse([], safe=False)

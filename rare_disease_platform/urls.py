from django.contrib import admin
from django.urls import path, include  # ✅ Import include to add app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ✅ Include URLs from api app
]

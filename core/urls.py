from django.contrib import admin
from django.urls import  path
from api_1.views import WomenAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist', WomenAPIView.as_view())
]

"""ProfeRate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rate.views import HandleAverageRequest, HandleListRequest, HandleLoginRequest, HandleLogoutRequest, HandleRateRequest, HandleRegisterRequest, HandleViewRequest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register',HandleRegisterRequest),
    path('api/login',   HandleLoginRequest),
    path('api/logout',  HandleLogoutRequest),
    path('api/list',    HandleListRequest),
    path('api/view',    HandleViewRequest),
    path('api/average', HandleAverageRequest),
    path('api/rate',    HandleRateRequest)
]



# Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'is_staff']

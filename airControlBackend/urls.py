"""airControlBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls import url
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r"^", include("products.urls")),
    url(r"^", include("accounts.urls")),
    url(r"login$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    url(r"^refresh-token$", TokenRefreshView.as_view(), name="token_refresh"),

    # # path('users/',views.UserViewSet.as_view()),
    # # path('groups/',views.GroupViewSet.as_view()),
    # # path('cities/get/',views.CityViewSet.as_view()),
    # # path('cities/create/',views.CityCreateView.as_view()),
    # # path('cities/delete/<pk>', views.CityDeleteView.as_view()),
    # # path('cities/update/<pk>', views.CityUpdateView.as_view()),
    # # path('countries/get/', views.CountryViewSet.as_view()),
    # # path('countries/create/', views.CountryCreateView.as_view()),
    # # path('countries/delete/<pk>', views.CountryDeleteView.as_view()),
    # # path('countries/update/<pk>', views.CountryUpdateView.as_view()),
    # # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # # path('api/accounts/', include("products.urls")),
]

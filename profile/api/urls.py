from django.urls import path
from rest_framework.authtoken import views
from .views import MyProfile, ProfileRUDAPIView, ProfileListCreateAPIView, CustomAuthToken


urlpatterns = [
    # path('', ProfileListCreateAPIView),
    # path('rud/<int:pk>/', ProfileRUDAPIView),
    # path('login/', views.obtain_auth_token),
    path('login/', CustomAuthToken.as_view()),
    path('my/profile/', MyProfile.as_view()),

]
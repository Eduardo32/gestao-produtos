from django.urls import path, include
from django.contrib.auth import views as auth_view
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
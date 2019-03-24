from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from accounts import views as accounts_view

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('signup/', accounts_view.SignUp.as_view(success_url=reverse_lazy('accounts:login')), name='signup'),
]
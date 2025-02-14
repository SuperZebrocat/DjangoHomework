from django.urls import path
from users.apps import UsersConfig

from .views import RegisterView
from django.contrib.auth.views import LogoutView
from users.views import CustomLoginView

app_name = 'UsersConfig.name'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(template_name='users/login.html', next_page='catalog:product_list'), name='login'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),

]

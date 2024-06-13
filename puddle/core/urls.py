from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy'),
    path('termofuse/',views.termofuse, name='termofuse'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('category/<int:category_id>/', views.category_detail_view, name='category_detail'),
]
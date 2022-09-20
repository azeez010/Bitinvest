from django.urls import path, include
from biti import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home_view, name="home"),
    path('home', views.home_menu, name="home-menu"),
    path('change-password', views.change_password_view, name="change-password"),
    path('login', views.login_view, name="login-view"),
    path('signup', views.signup_view, name="signup-view"),
    path('activate/<str:key_type>', views.activate_key, name="activate-key"),
    path('trade', views.trade, name="Trade"),
    path('partner', views.partner, name="Partner"),
    path('invest', views.invest, name="Invest")
]
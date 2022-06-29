
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
# from .views import SignUpView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.user_profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    path('changepass/',views.changepass,name='changepass'),
    path('thankyou/',views.thankyou,name='thankyou'),


    # path('sign-up/',SignUpView.as_view(),name='sign-up'),
    # path('sign-in/',SignInView.as_view(),name='sign-in'),
    # path('account-verify/<slug:token>',views.account_verify,name='account_verify'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

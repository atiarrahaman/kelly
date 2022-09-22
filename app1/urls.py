from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home , name='home'),
    path('about',views.About , name='about'),
    path('portfolio',views.Portfolio , name='portfolio'),
    path('resume',views.Resume , name='resume'),
    path('service',views.Service , name='service'),
    path('contact',views.Contact , name='contact'),
    path('registration',views.Registration , name='registration'),
    path('login',views.Login , name='login'),
    path('profile',views.Profile , name='profile'),
    path('logout',views.Logout , name='logout'),
    path('changepassword',views.Changepassword , name='changepassword'),
]+ static(settings.MEDIA_URL,
          document_root=settings.MEDIA_ROOT)

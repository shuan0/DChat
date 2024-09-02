from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

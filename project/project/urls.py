from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda _: redirect('home')),
    path('account/', include('account.urls')),
    path('chat/', include('chat.urls'))
]

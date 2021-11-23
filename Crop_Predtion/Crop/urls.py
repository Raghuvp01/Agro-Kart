from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('pred.urls')),
    path('admin/', admin.site.urls),
]

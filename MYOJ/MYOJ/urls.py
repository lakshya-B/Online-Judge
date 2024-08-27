from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include("members.urls")),
    path('submit/',include("compiler.urls")),
    path('',include("home.urls")),
]

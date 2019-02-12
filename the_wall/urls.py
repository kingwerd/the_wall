from django.urls import path, include

urlpatterns = [
    path('', include('apps.login_register.urls')),
    path('', include('apps.wall.urls'))
]

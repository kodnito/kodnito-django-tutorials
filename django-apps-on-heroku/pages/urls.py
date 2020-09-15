from django.urls import path

from .views import HelloWorld

app_name = 'pages'

urlpatterns = [
    path('', HelloWorld.as_view(), name='helloworld'),
]

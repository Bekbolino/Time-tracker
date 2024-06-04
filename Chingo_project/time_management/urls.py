from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_fun, name='login'),
    path("register", views.register, name='register'),
    path("main", views.main, name='main'),
    path("history", views.history, name='history'),
    path("logout", views.logout_fun, name='logout'),
    # path("light", views.light, name='light'),
]


# {% url 'имя пути' %} = url - обозначает путь и имя пути (имя пути в кавычках)
# {% load static %} = подключаем статик, дает возможность подключить статик
# {% static 'имя пути' %} = static - направляет на статик папку в котором есть css и javascript 
# {{ элемент }}
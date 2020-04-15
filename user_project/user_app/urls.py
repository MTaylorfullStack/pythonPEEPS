from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('process_mess', views.mess),
    path('all_users', views.show_users),
    path('all_mess', views.show_mess),
    path("add_like/<int:id>", views.add_like),
    path("view_mess/<int:id>", views.one_mess)
]
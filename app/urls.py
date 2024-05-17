from django.urls import path, include
from . import views
from .models import User

app_name = "app"
urlpatterns = [
    path('', views.user_list),
    path('add/', views.add_user),
    path('edit/<id>', views.edit_user),
    path('delete/<eid>', views.delete_user),
    path('view/<eid>', views.view_user),
]
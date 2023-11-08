from django.contrib import admin
from django.urls import path, include

from .views import register, login, logout, create_list, delete_task, update_task, retrieve_task

urlpatterns = [
    path("signup/", register),
    path('login/', login),
    path('logout/', logout),
    path("tasks/", create_list, name="create-list"),
    path("tasks/delete/<int:id>/", delete_task, name="delete-task"),
    path("tasks/update/<int:id>/", update_task, name="update-task"),
    path("tasks/<int:id>/", retrieve_task),

]
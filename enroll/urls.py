from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_show, name='add_show'),
    path("delete/<int:id>/", views.delete, name='delete'),
    path("updatestudent/<int:id>/", views.updatestudent, name='update'),
]

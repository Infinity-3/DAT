from django.urls import path
from . import views
urlpatterns = [
    path('',views.note, name='notes'),
    path('/update/<int:id>',views.update, name='update'),
    path('/delete/<int:id>',views.delete, name='delete'),
    path('/createnotes',views.create, name='createnotes'), 
]  
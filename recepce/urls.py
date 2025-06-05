from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('export-rezervace/', views.export_rezervace_to_excel, name='export_rezervace'),
]

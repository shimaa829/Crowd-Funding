from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.showProject),
    path('', views.create)
]


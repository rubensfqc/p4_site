
from django.urls import path
from . import views
urlpatterns=[
 path('',views.home),
 path('funcionalidades/',views.features),
 path('planos/',views.pricing),
 path('contato/',views.contact),
]

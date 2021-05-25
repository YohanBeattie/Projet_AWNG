from django.urls import path
from communitymanager import views

urlpatterns = [
    path('', views.home, name="accueil"),
    path('accueil', views.home),
    path('connexion', views.connexion),
    path('connexion2', views.home3),
    path('deconnexion', views.deconnexion, name='deconnexion'),


]

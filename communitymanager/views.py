from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django import forms


def home(request):
    return HttpResponse(""" 
    <h1> Réseau Supaerien </h1>
    <p> Tu peux t'inscrire dans les groupes que tu veux et participer à la vie étudiante ! </p>
    <p> <li><a href="communitymanager/connexion"> Se connecter </a></li> </p>
    """)


def home3(request):
    return render(request, 'communitymanager/connexion3.html')


def connexion(request):
    error = False
    if request.method == "POST":
        form = ConnexionForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)
            else:
                error=True
    else:
        form = ConnexionForm()

    return render(request, 'communitymanager/connexion3.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)



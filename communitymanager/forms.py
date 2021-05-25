from django import forms
from .models import Profil

"""class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username:")
    password = forms.PasswordInput()
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous "
                "souhaitez obtenir une copie du mail envoyé.",required=False)"""


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",max_length=30)
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput)

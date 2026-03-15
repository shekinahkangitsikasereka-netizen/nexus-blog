#---------------------------
#🧠 À quoi servent ces forms ? Ils vont être utilisés dans :📍 create_article.html

#pour publier un article #  📍 article_detail.html
#--------------------------------------------------------------

#  pour envoyer un commentaire
from django import forms
from .models import Article, Commentaire
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'tags']


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'image', 'tags']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# ===== TAG =====
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# ===== ARTICLE =====
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(default=timezone.now)

    # Image de l'article
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    # Tags liés
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)

    # Nombre de vues
    vues = models.PositiveIntegerField(default=0)

    # Likes
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="articles_likes",
        blank=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titre


# ===== COMMENTAIRE =====
class Commentaire(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="commentaires"
    )
    auteur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.auteur} sur {self.article}"
from django.urls import path
from . import views

app_name = "utilisateur"

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('create/', views.create_article, name='create_article'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path("like-ajax/", views.like_article_ajax, name="like_article_ajax"),
    path('edit/<int:id>/', views.edit_article, name='edit_article'),
    path('delete/<int:id>/', views.delete_article, name='delete_article'),
    
    # URL pour AJAX like
    path('like-ajax/', views.like_article_ajax, name='like_article_ajax'),

    # Connexion / Inscription / Profil
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profil/', views.profil, name='profil'),
    


    # Paramètres
    path('securite/', views.securite, name='securite'),
    path('apparence/', views.apparence, name='apparence'),
    path('langue/', views.langue, name='langue'),

]
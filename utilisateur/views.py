from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import Article, Commentaire
from .forms import ArticleForm, CommentaireForm, RegisterForm



from django.db.models import Count, F



# ===== ACCUEIL =====
def index(request):
    articles = Article.objects.all().order_by('-date_creation')
    return render(request, 'utilisateur/index.html', {'articles': articles})

# ===== DETAIL ARTICLE + COMMENTAIRES + VUES =====
def article_detail(request, id):
    article = get_object_or_404(Article, id=id)

    # augmenter les vues
    article.vues += 1
    article.save()

    return render(request, "utilisateur/article_detail.html", {"article": article})

    commentaires = article.commentaires.all().order_by('-date')
    form = CommentaireForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Vous devez être connecté pour commenter.")
            return redirect('utilisateur:login')

        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.auteur = request.user
            commentaire.article = article
            commentaire.save()
            messages.success(request, "Commentaire ajouté !")
            return redirect('utilisateur:article_detail', id=id)

    context = {
        'article': article,
        'commentaires': commentaires,
        'form': form
    }
    return render(request, 'utilisateur/article_detail.html', context)

# ===== CREER ARTICLE =====
@login_required
def create_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        article = form.save(commit=False)
        article.auteur = request.user
        article.save()
        messages.success(request, "Article publié avec succès !")
        return redirect('utilisateur:dashboard')
    return render(request, 'utilisateur/create_article.html', {'form': form})

# ===== EDITER ARTICLE =====
@login_required
def edit_article(request, id):
    article = get_object_or_404(Article, id=id, auteur=request.user)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Article modifié avec succès !")
        return redirect('utilisateur:dashboard')
    return render(request, 'utilisateur/edit_article.html', {'form': form, 'article': article})

# ===== SUPPRIMER ARTICLE =====
@login_required
def delete_article(request, id):
    article = get_object_or_404(Article, id=id, auteur=request.user)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Article supprimé !")
        return redirect('utilisateur:dashboard')
    return render(request, 'utilisateur/delete_article.html', {'article': article})

# ===== DASHBOARD =====
@login_required
def dashboard(request):
    articles = Article.objects.filter(auteur=request.user).order_by('-date_creation')
    return render(request, 'utilisateur/dashboard.html', {'articles': articles})

# ===== INSCRIPTION =====
def register(request):
    if request.user.is_authenticated:
        return redirect('utilisateur:dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Inscription réussie !")
        return redirect('utilisateur:dashboard')
    return render(request, 'utilisateur/register.html', {'form': form})

# ===== CONNEXION =====
def login_view(request):
    if request.user.is_authenticated:
        return redirect('utilisateur:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect('utilisateur:dashboard')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'utilisateur/login.html')

# ===== DECONNEXION =====
@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Déconnexion réussie.")
    return redirect('utilisateur:index')  # ← correspond au nom exact de l'URL

# ===== PROFIL =====
@login_required
def profil(request):
    articles = Article.objects.filter(auteur=request.user).order_by('-date_creation')
    return render(request, 'utilisateur/profil.html', {'user': request.user, 'articles': articles})

# ===== PARAMETRES =====
@login_required
def securite(request):
    return render(request, "utilisateur/securite.html")

@login_required
def apparence(request):
    return render(request, "utilisateur/apparence.html")

@login_required
def langue(request):
    return render(request, "utilisateur/langue.html")

# ===== LIKE ARTICLE =====
@login_required
def like_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.user in article.likes.all():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)
    return redirect('utilisateur:article_detail', id=id)

# ===== LIKE AJAX =====


@login_required
def like_article_ajax(request):
    if request.method == "POST":
        article_id = request.POST.get("article_id")
        article = Article.objects.get(id=article_id)

        if request.user in article.likes.all():
            article.likes.remove(request.user)
            liked = False
        else:
            article.likes.add(request.user)
            liked = True

        return JsonResponse({
            "liked": liked,
            "total_likes": article.likes.count()
        })




def index(request):

    articles = Article.objects.annotate(
        total_likes=Count('likes')
    ).annotate(
        popularity_score=F('total_likes') * 3 + F('vues')
    ).order_by('-popularity_score', '-date_creation')

    return render(request, "utilisateur/index.html", {"articles": articles})
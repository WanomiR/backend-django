from django.shortcuts import render, redirect
from .models import Article, Comment
from django.http import HttpResponseNotFound

# Create your views here.


def indexpage(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles, "page": "index"})


def aboutpage(request):
    return render(request, "about.html", {"page": "about"})


def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})

    else:
        print(request.POST)
        with open("/Users/vladbax6/Codding/code_works/Sites/Django/CourseBlog/Backend/blogsite/mainapp/contact_resuls.txt", "a") as file:
            file.writelines(f"Name: {request.POST['name']}, Email: {request.POST['email']}, Subject: {request.POST['subject']}")
        return redirect(contactpage)


def articlepage(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    if article:
        comments = Comment.objects.filter(Article=article).all()
        return render(request, "article.html", {"article": article, "comments": comments})

    return HttpResponseNotFound("Article not found")


def commentpost(request, article_id):
    if request.method == "POST":
        article = Article.objects.filter(id=article_id).first()
        if 'name' in request.POST and 'email' in request.POST and 'message' in request.POST:
            article.new_comment(request.POST)
            return redirect(articlepage, article_id)

    return HttpResponseNotFound("404")
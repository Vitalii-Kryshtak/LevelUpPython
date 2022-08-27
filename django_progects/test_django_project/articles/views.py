from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from articles.models import (
    Rubric,
    Tag,
    Article,
    Author,
)



def home(request: HttpRequest):
    rubrics = Rubric.objects.all()
    context = {"title": "Rubrics", "rubrics": rubrics}
    return render(request, "articles/rubrics.html", context=context)


def get_rubric(request: HttpRequest, pk):
    # tags = Tag.objects.all()
    # context = {"title": "Rubric Tags", "tags": tags}
    # return render(request, "articles/tags.html", context=context)
    rubric = Rubric.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Rubric: {rubric}")


def get_tags(request: HttpRequest):
    tags = Tag.objects.all()
    context = {"title": "Tags", "tags": tags}
    return render(request, "articles/tags.html", context=context)


def get_tag(request: HttpRequest, pk):
    tag = Tag.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Rubric: {tag}")


def get_all_articles(request: HttpRequest):
    articles = Article.objects.all()
    context = {"title": "Articles", "articles": articles}
    return render(request, "articles/articles.html", context=context)


def get_article(request: HttpRequest, pk):
    article = Article.objects.get(pk=pk)
    context = {"title": "Article",  "article": article}
    return render(request, "articles/article.html", context=context)


def get_all_authors(request: HttpResponse):
    authors =Author.objects.all()
    context = {"title": "Authors", "authors": authors}
    return render(request, "articles/authors.html", context=context)


def get_author_details(request: HttpRequest, pk):
    author = Author.objects.get(pk=pk)
    return HttpResponse(f"Mocked Page for Author: {author}")
from django.urls import path
from . import views

urlpatterns = [
    path("rubrics/", views.home, name="get_all_rubrics"),
    path("rubric/<int:pk>", views.get_rubric, name="get_rubric_details"),
    path("tags/", views.get_tags, name="get_all_tags"),
    path("tag/<int:pk>", views.get_tag, name="get_tag_details"),
    path("articles/", views.get_all_articles, name="get_all_articles"),
    path("article/<int:pk>", views.get_article, name="get_article"),
    path("authors/", views.get_all_authors, name="get_all_authors"),
    path("author/<int:pk>", views.get_author_details, name="get_author_details"),
]
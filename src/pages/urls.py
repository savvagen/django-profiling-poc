from django.urls import path, include
from .views import *
from .views import PagesView


urlpatterns = [
    path('', PagesView.home_view, name="home_page"),
    path('authors/', PagesView.authors_view, name='authors_page'),
    path("authors/<int:pk>/", PagesView.author_details, name="authors_detail_page"),
    path('articles/', PagesView.articles_view, name='articles_page'),
    path('articles/<int:pk>/', PagesView.article_details, name='articles_detail_page'),
    path("template/", PagesView.my_template, name="my_template"),

]

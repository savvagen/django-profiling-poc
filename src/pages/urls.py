from django.urls import path, include
from .views import *
from .views import PagesView


urlpatterns = [
    path('', PagesView.home_page_view, name="home_page"),
    path('authors/', PagesView.authors_list_view, name='authors_page'),
    path("authors/<int:id>/", PagesView.author_details_view, name="authors_detail_page"),
    path('articles/', PagesView.articles_list_view, name='articles_page'),
    path('articles/<int:id>/', PagesView.article_details_view, name='articles_detail_page'),
    path('articles/new/', PagesView.article_create_view, name='articles_create_page'),
    path('articles/search/', PagesView.article_search_view, name='search_page'),
    path('articles/<int:id>/delete/', PagesView.article_delete_view, name='article_delete_page'),
    path("template/", PagesView.my_template, name="my_template"),
]

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from author.models import Author
from author.serializers import AuthorSerializer
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.views import APIView


class PagesView(APIView):

    def home_view(request, *args, **kwargs):
        return render(request, "home.html", {})
        # return HttpResponse("""<h1>Home Page</h1>""")

    def authors_view(request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        context = {
            "authors": serializer.data,
            "description": "list of authors on this website"
        }
        return render(request, 'authors.html', context)

    def author_details(request, pk=None, *args, **kwargs):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        articles = Article.objects.filter(author=author)
        serializer = AuthorSerializer(author)
        context = {
            "author": serializer.data,
            "author_articles": articles
        }
        return render(request, 'author_details.html', context)

    def articles_view(request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        context = {
            "articles": serializer.data,
            "description": "list of articles on this website"
        }
        return render(request, 'articles.html', context)

    def article_details(request, pk=None, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article_ser = ArticleSerializer(article)
        author = get_object_or_404(Author.objects.all(), pk=article.author.pk)
        author_ser = AuthorSerializer(author)
        context = {
            "article": article_ser.data,
            "author": author_ser.data
        }
        return render(request, 'article_details.html', context)

    def my_template(request, *args, **kwargs):
        return render(request, "my_template.html", {})

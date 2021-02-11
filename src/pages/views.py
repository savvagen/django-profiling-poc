from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from author.models import Author
from author.serializers import AuthorSerializer
from article.models import Article
from article.serializers import ArticleSerializer
from rest_framework.views import APIView
from article.forms import ArticleForm, RawArticleForm
import random

class PagesView(APIView):

    def home_page_view(request, *args, **kwargs):
        return render(request, "home.html", {})
        # return HttpResponse("""<h1>Home Page</h1>""")

    def authors_list_view(request, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        context = {
            "authors": serializer.data,
            "description": "list of authors on this website"
        }
        return render(request, 'authors.html', context)

    def author_details_view(request, id=None, *args, **kwargs):
        author = get_object_or_404(Author.objects.all(), pk=id)
        articles = Article.objects.filter(author=author)
        serializer = AuthorSerializer(author)
        context = {
            "author": serializer.data,
            "author_articles": articles
        }
        return render(request, 'author_details.html', context)

    def articles_list_view(request, *args, **kwargs):
        title = request.POST.get("title")
        if title is not None:
            articles = Article.objects.filter(title=f"{title}")
            context = {"articles": articles, "description": "list of articles on this website"}
            return render(request, 'articles.html', context)
        else:
            articles = Article.objects.all()
            serializer = ArticleSerializer(articles, many=True)
            context = {"articles": serializer.data, "description": "list of articles on this website"}
            return render(request, 'articles.html', context)

    def article_details_view(request, id=None, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), pk=id)
        article_ser = ArticleSerializer(article)
        author = get_object_or_404(Author.objects.all(), pk=article.author.pk)
        author_ser = AuthorSerializer(author)
        context = {
            "article": article_ser.data,
            "author": author_ser.data
        }
        return render(request, 'article_details.html', context)

    def article_create_view(request, *args, **kwargs):
        initial_data = {'title': f'Test Article_{random.randint(000, 999)}', 'body': '<h1>Article Body</h1>'}
        form = ArticleForm(request.POST or None, initial=initial_data)
        # form = RawArticleForm(request.POST or None)
        if form.is_valid():
            art = form.save()
            # author = Author.objects.get(id=form.cleaned_data["author"])
            # data = {'title': form.cleaned_data["title"], 'subject': form.cleaned_data['subject'], 'body': form.cleaned_data['body'], 'author': author}
            # art = Article.objects.create(**data)
            #
            # 1. Redirect on the same form
            # form = ArticleForm()
            # 2. Make redirect
            return redirect('articles_detail_page', art.id)  # HttpResponseRedirect(f"/articles/{art.id}")
        context = {
            "form": form
        }
        return render(request, 'article_create.html', context)


    def article_delete_view(request, id=None, *args, **kwargs):
        article = get_object_or_404(Article.objects.all(), id=id)
        if request.method == "POST":
            article.delete()
            return redirect('articles_page')
        context = {"article": article}
        return render(request, 'article_delete.html', context)

    def article_search_view(request, *args, **kwargs):
        return render(request, 'article_search.html', {})

    def my_template(request, *args, **kwargs):
        return render(request, "my_template.html", {})

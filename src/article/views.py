from drf_yasg2.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from sentry_sdk import start_transaction
from author.models import Author
from author.serializers import AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    @swagger_auto_schema(responses={200: ArticleSerializer(many=False)})
    @action(methods=["GET"], detail=True)
    def get_full_info(self, request, pk=None, *args, **kwargs):
        with start_transaction(op="task", name="articles_get_full_info"):
            queryset = Article.objects.all()
            article = get_object_or_404(queryset, pk=pk)
            author = get_object_or_404(Author, id=article.author_id)
            article_data = ArticleSerializer(article).data
            author_data = AuthorSerializer(author).data
            article_data['author'] = author_data
            return Response(article_data, status=status.HTTP_200_OK)

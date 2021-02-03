from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

app_name = "articles"

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
urlpatterns = router.urls

# urlpatterns = [
#     path('articles/', ArticleView.as_view({'get': 'list'})),
#     path('articles/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
#     # url(r'^articles/(?P<pk>\d+)/$', ArticleView.as_view({'get': 'retrieve'})),
#     # url(r'^articles/', ArticleView.as_view({'get': 'list'})),
# ]


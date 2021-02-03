from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

app_name = "authors"

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
urlpatterns = router.urls

# urlpatterns = [
#     # path('authors/', AuthorView.as_view()),
#     # path('authors/<int:pk>', AuthorView.as_view()),
#     # url(r'^questions/(?P<pk>[\w:|-]+)/$', AuthorView.as_view()),
#     url(r'^authors/(?P<pk>\d+)/$', AuthorView.as_view()),
#     url(r'^authors/', AuthorView.as_view()),
#
# ]

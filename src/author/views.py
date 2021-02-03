from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

# Create your views here.
# class AuthorView(APIView):
#
#     # @silk_profile("get authors")
#     def get_authors(self):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response({'authors': serializer.data})
#
#     # @silk_profile("get author")
#     def get_author(self, pk):
#         author = get_object_or_404(Author.objects.all(), pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
#
#     def get(self, request, *args, **kwargs):
#         if request.method.lower() == "get" and self.kwargs.get('pk'):
#             return self.get_author(self.kwargs.get('pk'))
#         else:
#             return self.get_authors()
#
#     # @silk_profile(name='create author')
#     def post(self, request):
#         author = request.data.get('author')
#         # Create an article from the above data
#         serializer = AuthorSerializer(data=author)
#         if serializer.is_valid(raise_exception=True):
#             # author_saved = serializer.create()
#             author_saved = serializer.create(serializer.data)  # serializer.save()
#         return Response({"message": f"Author '{author_saved.name}' created successfully"}, status=201)
#
#     # @silk_profile(name='update author')
#     def put(self, request, pk):
#         with silk_profile(name='Update Author #%s' % pk):
#             saved_author = get_object_or_404(Author.objects.all(), pk=pk)
#             data = request.data.get('author')
#             serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)
#             if serializer.is_valid(raise_exception=True):
#                 author_saved = serializer.update(instance=saved_author, validated_data=data)  # serializer.save()
#             return Response({"message": f"Author '{author_saved.name}' updated successfully"})
#
#     # @silk_profile(name='delete author')
#     def delete(self, request, pk):
#         author = get_object_or_404(Author.objects.all(), pk=pk)
#         author.delete()
#         return Response({"message": "Author with id `{}` has been deleted.".format(pk)}, status=204)

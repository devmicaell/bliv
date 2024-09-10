from rest_framework import viewsets
from bliv_app.api import serializers
from bliv_app import models

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BooksSerializer
    queryset = models.Books.objects.all()
# from django.shortcuts import render
from rest_framework import generics, permissions, authentication
from collection.models import Book
import collection.serializers as serializers

# Create your views here.


class AddBookView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    permission_classes = (permissions.IsAdminUser,)
    # authentication_classes = (authentication.TokenAuthentication,)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    permission_classes = (permissions.AllowAny,)


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookUpdateSerializer

    permission_classes = (permissions.IsAdminUser,)
    # authentication_classes = (authentication.TokenAuthentication,)


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.DeletionSerializer

    permission_classes = (permissions.IsAdminUser,)
    # authentication_classes = (authentication.TokenAuthentication,)


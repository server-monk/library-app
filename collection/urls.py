from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.AddBookView.as_view(), name='add'),
    path('books/', views.BookListView.as_view(), name='all-books'),
    path('book/update/', views.BookUpdateView.as_view(), name='update'),
    path('book/delete/', views.BookDeleteView.as_view(), name='delete'),
    # path('book/<int:pk>/', BookDetailView.as_view(), name='profile'),
]
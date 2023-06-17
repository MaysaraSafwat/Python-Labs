from django.urls import path
from . import views


urlpatterns = [
    path('index/' , views.index , name="book-list"),
    path('book_details/<int:book_id>/', views.get_book_details, name="book-details"),
    path('book_update/<int:book_id>/', views.update, name="book-update")
]
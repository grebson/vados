from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='articles'),
    path('create/', create_view, name='create-article'),
    path('<str:pk>/', detail_view, name='article'),
    path('<str:pk>/update/', update_view, name='update-article'),
    path('<str:pk>/delete/', delete_view, name='delete-article'),
    path('category/<str:pk>/', category_view, name='category'),
]

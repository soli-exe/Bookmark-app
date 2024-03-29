from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('',
         TemplateView.as_view(template_name='home.html'), name='home'),
    path('bookmarks/',
         views.BookmarkListView.as_view(), name='index'),
    path('delete/<int:pk>/',
         views.BookmarkDeleteView.as_view(), name='delete_bookmark'),
    path('edit/<int:pk>/',
         views.BookmarkUpdateView.as_view(), name='edit_bookmark'),
    path('add/', views.BookCreateView.as_view(), name='add_bookmark'),
    path('search/', views.SearchView.as_view(), name='search'),

]

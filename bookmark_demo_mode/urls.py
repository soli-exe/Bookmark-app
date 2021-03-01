from django.urls import path
from bookmark_demo_mode import views

app_name = 'bookmark_demo_mode'

urlpatterns = [
    path('bookmark-demo-list/', views.DemoIndex.as_view(), name='demo_index'),
    path('bookmark-demo-add', views.DemoBookmarkAddView.as_view(),
         name='demo_bookmark_add'),
    path('bookmark-demo-delete/<int:pk>/', views.DemoBookmarkDeleteView.as_view(),
         name='demo_bookmark_delete'),
    path('bookmark-demo-edit/<int:pk>/', views.DemoBookmarkUpdateView.as_view(),
         name='demo_bookmark_edit'),

]

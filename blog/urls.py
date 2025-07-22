"""
URL configuration for the blog application.
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('tag/<slug:slug>/', views.tag_posts, name='tag_posts'),
    path('comment/<int:comment_id>/edit/',
         views.comment_edit, name='comment_edit'),
    path('comment/<int:comment_id>/delete/',
         views.comment_delete, name='comment_delete'),
    path('comment/<int:comment_id>/delete-ajax/',
         views.comment_delete_ajax, name='comment_delete_ajax'),
]

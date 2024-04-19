from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blogs/', views.blogs, name="blogs"),
    path('catagory_blog/<str:slug>', views.catagory_blog, name="catagory_blog"),
    path('tag_blogs/<str:slug>', views.tag_blogs, name="tag_blogs"),
    
    path('blog_details/<str:slug>', views.blog_details, name="blog_details"),
    path("add_reply/<int:blog_id>/<int:comment_id>/", views.add_reply, name="add_reply"),
    path("search_blog/", views.search_blog, name="search_blog"),

]

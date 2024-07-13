from django.urls import path
from . import views 
urlpatterns=[
    # path('',views.home,name="blog-home"),
    path('home/',views.home,name="blog-home"),
    # path("",views.home,name="blog-home"),
    path("",views.createListView.as_view(),name="blog-home"),
    path("about/",views.about,name="blog-about"),
    path("post/addpost/",views.addPostView.as_view(),name="post-add"),
    path('post/<int:pk>/update/',views.updatePostView.as_view(),name="post-update"),
    path('post/<int:pk>/delete/',views.deletePostView.as_view(),name="post-delete"),
    path('post/<int:pk>/detail/',views.postDetailView.as_view(),name="post-detail"),

]
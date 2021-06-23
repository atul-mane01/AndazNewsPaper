from django.contrib import admin
from django.urls import path
from andaz import views
urlpatterns = [
   path("", views.index, name='index'),
   # url('blogsingle',blogsingle,name='blog-single'),
   # url('blog',blog,name='blog'),
   # url('contact',contact,name='contact'),
   # url('features',features,name='features'),
   # url('pricing',pricing,name='pricing'),
]

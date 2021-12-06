from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.newsBlog, name='news'),
    path('search', views.searchBlog, name='search'),
    path('detail/<str:pk>', views.detailBlog, name='detail-blog'),

    path('update', views.updateBlog, name='update-blog'),
    path('delete/<str:pk>', views.delete_Blog, name='delete-blog'),
]

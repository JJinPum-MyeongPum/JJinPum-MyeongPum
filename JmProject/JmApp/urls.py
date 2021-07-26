from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),   
    path('detail/<str:id>', views.detail, name='detail'), 
    path('edit/<str:id>', views.edit, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('mypage/<str:username>', views.mypage, name='mypage'), 
    path('create_comment/<str:item_id>/<str:username>', views.create_comment, name="create_comment"),
    path('delete_comment/<str:item_id>/<str:comment_id>', views.delete_comment, name="delete_comment"),
    path('update_comment/<str:item_id>/<str:comment_id>', views.update_comment, name="update_comment"),
]

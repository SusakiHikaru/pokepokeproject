from django.urls import path
from . import views

#URLパターンを逆引きできるよう名前をつける
app_name = 'pokepoke'

#URLパターンを登録する変数
urlpatterns = [
    #pokepokeアプリのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    #投稿完了ページへのアクセス
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
]
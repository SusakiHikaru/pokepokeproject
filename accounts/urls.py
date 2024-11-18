from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

#URLパターンを登録するための変数
urlpatterns = [
    #サインアップページのビュー呼び出し
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #サインアップ完了ページのビュー呼び出し
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    #ログインページの表示
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #ログアウトを実行
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    #カテゴリ名のフィールド
    title = models.CharField(verbose_name='カテゴリ', max_length=20)

    def __str__(self):
        '''オブジェクトを文字列にして返す
        '''
        return self.title
    
class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    #ユーザフィールド
    user = models.ForeignKey(CustomUser,verbose_name='ユーザ', on_delete=models.CASCADE)
    #カテゴリフィールド
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    #タイトル用のフィールド
    title = models.CharField(verbose_name='タイトル', max_length=200)
    #コメント用のフィールド
    comment = models.TextField(verbose_name='コメント')
    #イメージのフィールド
    image1 = models.ImageField(verbose_name='イメージ１', upload_to='photos')
    #イメージのフィールド
    image2 = models.ImageField(verbose_name='イメージ２', upload_to='photos', blank=True, null=True)
    #投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)

    def __str__(self):
        '''オブジェクトを文字列に変換して返す
        '''
        return self.title


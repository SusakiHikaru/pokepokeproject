from django.forms import ModelForm
from .models import PhotoPost

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        '''
        model = PhotoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2']
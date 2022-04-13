from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs = {
                'class':'my-title form-control',
                'placeholder':'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget = forms.Textarea(
            attrs = {
                'class':'my-content form-control',
                'placeholder':'Enter the content',
                'rows':5,
                'cols':50,
            }
        ),
        error_messages = {
            'required': 'please enter your content'
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 이렇게 받으면 외래키 필드를 직접 작성하게 해야됨
        # 그러면 2번 게시글에서 1번 게시글 댓글을 달 수 있게 만들어줌
        # fields = '__all__'
        # 따라서 content만 직접 지정할 수 있도록 해야함
        exclude = ('article',)
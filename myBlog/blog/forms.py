from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control inputs'}),
            'title': forms.TextInput(attrs={'class': 'form-control inputs'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control inputs'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

    widgets = {
        'author': forms.TextInput(attrs={'class': 'form-control'}),
        'text': forms.Textarea(attrs={'class': 'form-control '})
    }




from django import forms
from .models import Post,Profile, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }




class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['f_name', 'l_name', 'profile_pic', 'contact_info']
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'contact_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter contact details'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Write a comment...'}),
        }
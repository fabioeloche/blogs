"""
Forms for the blog application.
"""
from django import forms
from django.contrib.auth import get_user_model
from .models import Comment

User = get_user_model()


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments."""
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your comment here...',
            }),
        }


class EmailChangeForm(forms.Form):
    """Form for changing user email address."""
    
    new_email = forms.EmailField(
        label='New Email Address',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your new email address',
        }),
        help_text='Enter the new email address you want to use for your account.'
    )
    
    confirm_email = forms.EmailField(
        label='Confirm New Email',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your new email address',
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        new_email = cleaned_data.get('new_email')
        confirm_email = cleaned_data.get('confirm_email')
        
        if new_email and confirm_email:
            if new_email != confirm_email:
                raise forms.ValidationError(
                    "The two email addresses don't match. Please try again."
                )
            
            # Check if email is already in use
            if User.objects.filter(email=new_email).exists():
                raise forms.ValidationError(
                    "This email address is already in use. Please use a different email."
                )
        
        return cleaned_data

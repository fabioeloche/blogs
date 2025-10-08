"""
Views for user account management.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import EmailChangeForm


@login_required
def account_settings(request):
    """
    Display account settings page with user information and handle email changes.
    """
    if request.method == 'POST':
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            old_email = request.user.email
            
            # Update user email
            request.user.email = new_email
            request.user.save()
            
            messages.success(
                request,
                f'Your email has been successfully changed from {old_email} to {new_email}.'
            )
            return redirect('account_settings')
    else:
        form = EmailChangeForm()
    
    context = {
        'form': form,
    }
    return render(request, 'account/email.html', context)


@login_required
def account_delete_confirm(request):
    """
    Display account deletion confirmation page.
    """
    return render(request, 'account/account_delete_confirm.html')


@require_POST
@login_required
def account_delete(request):
    """
    Delete user account permanently.
    """
    user = request.user
    username = user.username or user.email
    
    # Log out the user
    logout(request)
    
    # Delete the user account
    user.delete()
    
    messages.success(
        request,
        f'Your account has been successfully deleted. We\'re sorry to see you go!'
    )
    
    return redirect('blog:post_list')


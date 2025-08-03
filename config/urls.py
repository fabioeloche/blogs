"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.account import views as allauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Custom allauth URLs excluding password reset
    path('accounts/login/', allauth_views.LoginView.as_view(), name='account_login'),
    path('accounts/signup/', allauth_views.SignupView.as_view(), name='account_signup'),
    path('accounts/logout/', allauth_views.LogoutView.as_view(), name='account_logout'),
    path('accounts/email/', allauth_views.EmailView.as_view(), name='account_email'),
    path('accounts/confirm-email/', allauth_views.EmailVerificationSentView.as_view(), name='account_email_verification_sent'),
    path('accounts/confirm-email/<key>/', allauth_views.ConfirmEmailView.as_view(), name='account_confirm_email'),
    # Exclude password reset URLs - they are now disabled
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls')),
    path('about/', include('about.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

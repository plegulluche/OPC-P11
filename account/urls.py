from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.registration_view, name="add_user"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("account/", views.account_view, name="account_page"),
    # Activate account
    path("activate-email/<slug:token>", views.activate_email_view, name="activate"),
    path("success", views.active_succes_view, name="success"),
    path("activate-message", views.activate_message_view, name="activate_your_mail"),
    # Reset password
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset/password_reset_form.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset/password_reset_confirm_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset/password_change_done.html"
        ),
        name="password_reset_complete",
    ),
    # Password change
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="password_reset/password_change.html"
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeView.as_view(
            template_name="password_reset/password_change_done.html"
        ),
        name="password_change_done",
    ),
]

from django.urls import path
from accounts import views
from django.contrib import auth

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('change/password/', views.change_password, name='change_password'),
    path('password-reset/', auth.views.PasswordResetView.as_view(),
         name='passowrd_reset'),
    path('password-reset/done/', auth.views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth.views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth.views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete')
]

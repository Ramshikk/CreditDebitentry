from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('Amount',views.credit_debit_entry),
    path('journalentryview',views.entry_view),
    path("accounts/",include("django.contrib.auth.urls")),
]

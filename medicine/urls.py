from django.contrib import admin
from django.urls import path
from portal import views

urlpatterns = [
    path("", views.index, name="home"),
]


handler404 = "portal.views.page_not_found_view"
handler403 = "portal.views.page_forbidden"
handler400 = "portal.views.page_bad_request"
#handler500 = "messenger.views.page_internal_server"
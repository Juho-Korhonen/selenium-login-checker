from django.urls import path
from .views import display_about_me_page,display_contact_page
urlpatterns = [
    path('about-me',display_about_me_page),
    path('contact',display_contact_page)
]
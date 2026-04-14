from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("testimonials/submit/", views.submit_testimonial, name="submit_testimonial"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("team/", views.team, name="team"),
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("appointment/", views.appointment, name="appointment"),
    path("contact/", views.contact, name="contact"),
]


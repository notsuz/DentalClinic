from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import AppointmentRequestForm, ContactMessageForm, PublicTestimonialForm
from .models import BlogPost, FAQ, GalleryImage, Service, TeamMember, Testimonial


def home(request):
    services = Service.objects.all()[:6]
    featured_services = Service.objects.filter(featured=True)[:6]
    team = TeamMember.objects.filter(active=True)[:6]
    testimonials = (
        Testimonial.objects.filter(approved=True)
        .order_by("-featured", "sort_order", "-created_at")[:6]
    )
    faqs = FAQ.objects.filter(active=True)[:8]
    gallery = GalleryImage.objects.filter(active=True)[:8]
    posts = BlogPost.objects.filter(published=True)[:3]

    return render(
        request,
        "index.html",
        {
            "services": services,
            "featured_services": featured_services,
            "team": team,
            "testimonials": testimonials,
            "faqs": faqs,
            "gallery": gallery,
            "posts": posts,
            "testimonial_form": PublicTestimonialForm(),
        },
    )


def services(request):
    return render(request, "website/services.html", {"services": Service.objects.all()})


def team(request):
    return render(
        request,
        "website/team.html",
        {"team": TeamMember.objects.filter(active=True)},
    )


def about(request):
    return render(request, "website/about.html")


def blog_list(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, "website/blog_list.html", {"posts": posts})


def blog_detail(request, slug: str):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, "website/blog_detail.html", {"post": post})


@require_http_methods(["GET", "POST"])
def appointment(request):
    if request.method == "POST":
        form = AppointmentRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks — we received your request. We’ll contact you shortly to confirm your appointment.",
            )
            return redirect("appointment")
    else:
        form = AppointmentRequestForm()

    return render(request, "website/appointment.html", {"form": form})


@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent. We’ll get back to you soon.")
            return redirect("contact")
    else:
        form = ContactMessageForm()

    return render(request, "website/contact.html", {"form": form})


@require_http_methods(["POST"])
def submit_testimonial(request):
    form = PublicTestimonialForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(
            request,
            "Thanks for your feedback! Your review was submitted and will appear after approval.",
        )
    else:
        messages.error(request, "Please fix the errors and try again.")
    return redirect("home")


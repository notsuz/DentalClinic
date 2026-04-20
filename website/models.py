from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SiteSettings(TimeStampedModel):
    site_name = models.CharField(max_length=120, default="Tuyou Dental")
    tagline = models.CharField(
        max_length=220, default="Modern dentistry with a gentle touch."
    )
    phone = models.CharField(max_length=40, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    address = models.CharField(max_length=220, blank=True, default="")

    hero_title = models.CharField(max_length=120, default="Healthy smiles start here.")
    hero_subtitle = models.TextField(
        default="From checkups to cosmetic care, we make every visit calm, clear, and comfortable."
    )
    hero_primary_cta_text = models.CharField(max_length=40, default="Book Appointment")
    hero_primary_cta_url = models.CharField(max_length=120, default="/appointment/")
    hero_secondary_cta_text = models.CharField(max_length=40, default="View Services")
    hero_secondary_cta_url = models.CharField(max_length=120, default="/services/")

    # hero_image_url = models.URLField(blank=True, default="")
    hero_image = models.ImageField(upload_to="hero/", null= True, blank= True)
    about_title = models.CharField(max_length=120, default="Trusted care for every stage.")
    about_body = models.TextField(
        default=(
            "Welcome to TuYou Dental Care, where brightening your smile brightens our day.\n\n"
            "We offer a comprehensive range of treatments, from routine cleanings and preventative care "
            "to advanced cosmetic, prosthetic and restorative procedures. We believe in personalized care "
            "tailored to meet the unique needs of each patient, ensuring a comfortable and stress-free experience.\n\n"
            "Our state-of-the-art facility is equipped with the latest technology to deliver the highest standard "
            "of dental care. Trust TuYou Dental Care to help you achieve and maintain a healthy, beautiful smile.\n\n"
            "\"We Cure With full cure\""
        )
    )
    # about_image_url = models.URLField(blank=True, default="")
    about_image = models.ImageField(upload_to="about/", null= True, blank= True)

    opening_hours = models.TextField(
        blank=True,
        default="Mon–Fri: 8:00–18:00\nSat: 9:00–14:00\nSun: Closed",
        help_text="One line per entry.",
    )

    social_facebook = models.URLField(blank=True, default="")
    social_instagram = models.URLField(blank=True, default="")
    social_x = models.URLField(blank=True, default="")

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self) -> str:
        return self.site_name

    @classmethod
    def get_solo(cls):
        obj, _created = cls.objects.get_or_create(pk=1)
        return obj


class Service(TimeStampedModel):
    title = models.CharField(max_length=120)
    short_description = models.CharField(max_length=220, blank=True, default="")
    description = models.TextField(blank=True, default="")
    icon_image = models.ImageField(
        upload_to="service-icons/",
        blank=True,
        null=True,
        help_text="Upload a small icon image (PNG preferred). Recommended size: ~64x64.",
    )
    featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["sort_order", "title"]

    def __str__(self) -> str:
        return self.title


class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True, default="")
    bio = models.TextField(blank=True, default="")
    photo = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True,
        help_text="Upload a profile photo (square image recommended).",
    )
    sort_order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "name"]

    def __str__(self) -> str:
        return self.name


class Testimonial(TimeStampedModel):
    author_name = models.CharField(max_length=120)
    author_title = models.CharField(max_length=120, blank=True, default="")
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    featured = models.BooleanField(default=False)
    approved = models.BooleanField(
        default=True,
        help_text="If unchecked, this testimonial will not be shown on the public website.",
    )
    sort_order = models.PositiveIntegerField(default=100)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self) -> str:
        return f"{self.author_name} ({self.rating}/5)"


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=220)
    answer = models.TextField()
    sort_order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "question"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self) -> str:
        return self.question

class GalleryImage(TimeStampedModel):
    title = models.CharField(max_length=120, blank=True, default="")
    image = models.ImageField(upload_to="gallery/" , null=True, blank=True) 
    caption = models.CharField(max_length=220, blank=True, default="")
    sort_order = models.PositiveIntegerField(default=100)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self) -> str:
        # Update the __str__ to use the new field name
        return self.title or f"Image {self.id}"


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    excerpt = models.CharField(max_length=280, blank=True, default="")
    body = models.TextField()
    cover_image_url = models.URLField(blank=True, default="")
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)[:200] or "post"
            slug = base
            i = 2
            while BlogPost.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base}-{i}"
                i += 1
            self.slug = slug
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class AppointmentRequest(TimeStampedModel):
    full_name = models.CharField(max_length=160)
    phone = models.CharField(max_length=40)
    email = models.EmailField(blank=True, default="")
    preferred_date = models.DateField(blank=True, null=True)
    preferred_time = models.CharField(max_length=60, blank=True, default="")
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, blank=True, null=True
    )
    message = models.TextField(blank=True, default="")
    status = models.CharField(
        max_length=30,
        default="new",
        choices=[
            ("new", "New"),
            ("contacted", "Contacted"),
            ("scheduled", "Scheduled"),
            ("closed", "Closed"),
        ],
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.status})"


class ContactMessage(TimeStampedModel):
    full_name = models.CharField(max_length=160)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True, default="")
    subject = models.CharField(max_length=200, blank=True, default="")
    message = models.TextField()
    status = models.CharField(
        max_length=30,
        default="new",
        choices=[("new", "New"), ("replied", "Replied"), ("closed", "Closed")],
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.full_name} ({self.email})"

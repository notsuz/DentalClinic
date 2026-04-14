from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import BlogPost, FAQ, Service, SiteSettings, TeamMember, Testimonial


@receiver(post_migrate)
def ensure_seed_data(sender, **kwargs):
    # Only seed our own app.
    if getattr(sender, "name", None) != "website":
        return

    settings_obj = SiteSettings.get_solo()
    old_default = (
        "We combine modern equipment, clear communication, and a gentle approach so you always know what’s next."
    )
    if settings_obj.about_body.strip() == old_default:
        settings_obj.about_body = SiteSettings._meta.get_field("about_body").default
        settings_obj.save(update_fields=["about_body", "updated_at"])

    if not Service.objects.exists():
        Service.objects.bulk_create(
            [
                Service(
                    title="Dental Checkup",
                    short_description="Routine exams, cleanings, and prevention.",
                    featured=True,
                    sort_order=10,
                ),
                Service(
                    title="Teeth Whitening",
                    short_description="Brighten your smile safely and effectively.",
                    featured=True,
                    sort_order=20,
                ),
                Service(
                    title="Dental Implants",
                    short_description="Natural-looking replacements for missing teeth.",
                    featured=False,
                    sort_order=30,
                ),
                Service(
                    title="Braces & Aligners",
                    short_description="Orthodontic options for every lifestyle.",
                    featured=False,
                    sort_order=40,
                ),
                Service(
                    title="Emergency Care",
                    short_description="Same-day help when you need it most.",
                    featured=True,
                    sort_order=15,
                ),
                Service(
                    title="Cosmetic Dentistry",
                    short_description="Veneers, bonding, and smile makeovers.",
                    featured=False,
                    sort_order=50,
                ),
            ]
        )

    if not TeamMember.objects.exists():
        TeamMember.objects.bulk_create(
            [
                TeamMember(
                    name="Dr. Amina Tuyou",
                    role="Lead Dentist",
                    bio="Patient-first care focused on comfort, clarity, and long-term oral health.",
                    sort_order=10,
                    active=True,
                ),
                TeamMember(
                    name="Dr. Kelvin Mensah",
                    role="Dental Surgeon",
                    bio="Advanced restorative treatments with a gentle approach.",
                    sort_order=20,
                    active=True,
                ),
                TeamMember(
                    name="Nana Owusu",
                    role="Dental Hygienist",
                    bio="Prevention, cleanings, and coaching for healthier daily habits.",
                    sort_order=30,
                    active=True,
                ),
            ]
        )

    if not Testimonial.objects.exists():
        Testimonial.objects.bulk_create(
            [
                Testimonial(
                    author_name="Sarah K.",
                    author_title="Patient",
                    quote="The team was calm and professional. I finally feel confident about my smile.",
                    rating=5,
                    featured=True,
                    sort_order=10,
                ),
                Testimonial(
                    author_name="Daniel A.",
                    author_title="Patient",
                    quote="Clear explanations, no pressure, and a great result. Highly recommended.",
                    rating=5,
                    featured=True,
                    sort_order=20,
                ),
                Testimonial(
                    author_name="Ama B.",
                    author_title="Patient",
                    quote="Best dental experience I’ve had. Quick, clean, and comfortable.",
                    rating=5,
                    featured=False,
                    sort_order=30,
                ),
            ]
        )

    if not FAQ.objects.exists():
        FAQ.objects.bulk_create(
            [
                FAQ(
                    question="Do you accept walk-ins?",
                    answer="We recommend booking ahead, but we’ll always try to accommodate urgent cases.",
                    sort_order=10,
                    active=True,
                ),
                FAQ(
                    question="How often should I get a checkup?",
                    answer="Most patients benefit from a checkup and cleaning every 6 months.",
                    sort_order=20,
                    active=True,
                ),
                FAQ(
                    question="Is whitening safe?",
                    answer="Yes — we use evidence-based methods and tailor treatment to your teeth and sensitivity.",
                    sort_order=30,
                    active=True,
                ),
                FAQ(
                    question="Do you offer emergency dental care?",
                    answer="Yes. If you’re in pain, contact us and we’ll prioritize same-day support when possible.",
                    sort_order=40,
                    active=True,
                ),
            ]
        )

    if not BlogPost.objects.exists():
        BlogPost.objects.create(
            title="5 habits for a healthier smile",
            excerpt="Small daily changes that protect your teeth and gums.",
            body=(
                "Healthy smiles are built day by day. Start with consistent brushing and flossing, "
                "choose water often, and keep regular checkups so small issues don’t become big ones."
            ),
            published=True,
        )


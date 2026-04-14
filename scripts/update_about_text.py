import sys
import os

import django


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuyoudental.settings")
    django.setup()

    from website.models import SiteSettings  # noqa: PLC0415

    s = SiteSettings.get_solo()
    s.about_body = (
        "Welcome to TuYou Dental Care, where brightening your smile brightens our day.\n\n"
        "We offer a comprehensive range of treatments, from routine cleanings and preventative care "
        "to advanced cosmetic, prosthetic and restorative procedures. We believe in personalized care "
        "tailored to meet the unique needs of each patient, ensuring a comfortable and stress-free experience.\n\n"
        "Our state-of-the-art facility is equipped with the latest technology to deliver the highest standard "
        "of dental care. Trust TuYou Dental Care to help you achieve and maintain a healthy, beautiful smile.\n\n"
        "\"We Cure With full cure\""
    )
    s.save()
    print("updated")


if __name__ == "__main__":
    main()


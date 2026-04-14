import os
import sys

import django


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tuyoudental.settings")
    django.setup()

    from website.models import SiteSettings  # noqa: PLC0415

    s = SiteSettings.get_solo()
    s.phone = "9851364688 / 9841873042"
    s.address = "Bhanimandal, Lalitpur"
    s.save()
    print("updated")


if __name__ == "__main__":
    main()


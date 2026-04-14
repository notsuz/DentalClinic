from .models import SiteSettings


def site_settings(request):
    settings_obj = SiteSettings.get_solo()
    return {"site_settings": settings_obj}


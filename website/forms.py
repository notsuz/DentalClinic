from django import forms

from .models import AppointmentRequest, ContactMessage, Testimonial


class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = [
            "full_name",
            "phone",
            "email",
            "preferred_date",
            "preferred_time",
            "service",
            "message",
        ]
        widgets = {
            "preferred_date": forms.DateInput(attrs={"type": "date"}),
            "message": forms.Textarea(attrs={"rows": 4}),
        }


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "phone", "subject", "message"]
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}


class PublicTestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["author_name", "rating", "quote"]
        widgets = {"quote": forms.Textarea(attrs={"rows": 4})}

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.approved = False
        obj.featured = False
        if commit:
            obj.save()
        return obj


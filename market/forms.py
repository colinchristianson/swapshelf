from django.contrib.auth.models import User
from django import forms

from market.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "price", "category", "seller_note"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        # is_staff is a privilege flag (desk + /admin/ access). It must never be
        # user-editable; grant it from the Django admin or a management command.
        fields = ["first_name", "last_name", "email"]

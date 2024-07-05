from django import forms
from .models import Booking, Room

class AvailabilityForm(forms.Form):
    check_in = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    check_out = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    room_type = forms.ModelChoiceField(queryset=Room.objects.all(), empty_label="Select Room Type")


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest_name', 'guest_email', 'guest_phone', 'check_in', 'check_out']

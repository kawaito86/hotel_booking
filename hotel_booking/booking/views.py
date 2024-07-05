from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Room, Booking, PricingRule
from .forms import AvailabilityForm, BookingForm
from django.contrib import messages
import uuid
from django.core.mail import send_mail
import logging
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP


def home(request):
    form = AvailabilityForm()
    return render(request, 'booking/home.html', {'form': form})



def check_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']
            room_type = form.cleaned_data['room_type']

            # Debugging: print out form data
            print(f"Check-in: {check_in}, Check-out: {check_out}, Room Type: {room_type}")

            # Print all rooms
            all_rooms = Room.objects.all()
            print(f"All Rooms: {all_rooms}")

            # Filter rooms by type and availability
            rooms = Room.objects.filter(room_type=room_type.room_type, is_available=True)

            # Debugging: print out filtered rooms by type and availability
            print(f"Filtered Rooms by Type and Availability: {rooms}")

            # Exclude rooms that have overlapping booking
            available_rooms = rooms.exclude(
                Q(booking__check_in__lt=check_out) & Q(booking__check_out__gt=check_in)
            ).distinct()

            # Debugging: print out available rooms
            print(f"Available Rooms: {available_rooms}")

            message = None

            # If no rooms of the selected type are available, get all available rooms
            if not available_rooms.exists():
                message = "Your selected room type is not available. Here are other available rooms."
                available_rooms = Room.objects.filter(is_available=True).exclude(
                    Q(booking__check_in__lt=check_out) & Q(booking__check_out__gt=check_in)
                ).distinct()

            # Debugging: print out fallback available rooms
            print(f"Fallback Available Rooms: {available_rooms}")

            return render(request, 'booking/check_availability.html', {
                'rooms': available_rooms,
                'check_in': check_in,
                'check_out': check_out,
                'message': message
            })
    else:
        form = AvailabilityForm()

    return redirect('home')

logger = logging.getLogger(__name__)

def book_room(request, room_id):
    room = Room.objects.get(id=room_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()

            # Send confirmation email to the guest
            subject = 'Booking Confirmation for {}'.format(room.room_type)
            message = (
                f'Dear {booking.guest_name},\n\n'
                f'Your booking for {room.room_type} - Room Number {room.room_number} has been confirmed.\n\n'
                f'Booking Number: {booking.booking_number}\n'
                f'Check-in Date: {form.cleaned_data["check_in"]}\n'
                f'Check-out Date: {form.cleaned_data["check_out"]}\n'
                f'Total Nights: {(form.cleaned_data["check_out"] - form.cleaned_data["check_in"]).days}\n'
                f'Total Price: {room.get_adjusted_price() * (form.cleaned_data["check_out"] - form.cleaned_data["check_in"]).days}\n\n'  # Corrected here
                f'Please note that the room will be charged at the rate of {room.get_adjusted_price()} per night.\n\n'  # Corrected here
                'Thank you for choosing our hotel. We look forward to welcoming you!\n\n'
                'Best regards,\n'
                'NANA'
            )
            
            sender_email = settings.EMAIL_HOST_USER  # Update with your email settings
            recipient_email = booking.guest_email  # Assuming guest_email is part of your form

            send_mail(subject, message, sender_email, [recipient_email])

            # Pop up a success message
            messages.success(request, 'Your booking has been made successfully! A confirmation email has been sent to you.')

            return redirect('home')
    else:
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        initial_data = {
            'room': room,
            'check_in': check_in,
            'check_out': check_out
        }
        form = BookingForm(initial=initial_data)

    return render(request, 'booking/book_room.html', {'form': form, 'room': room})



def room_details(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    context = {
        'room': room
    }
    return render(request, 'booking/room_details.html', context)
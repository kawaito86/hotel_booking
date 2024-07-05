from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check_availability/', views.check_availability, name='check_availability'),
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path("room_details/<int:room_id>/", views.room_details, name="room_details"),
]
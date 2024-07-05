from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Optionally, add additional template directories here
        'APP_DIRS': True,
        'OPTIONS': {
            # Other options...
        },
    },
]
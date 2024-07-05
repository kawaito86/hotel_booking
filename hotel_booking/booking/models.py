from django.db import models
import uuid
from django.utils import timezone
from decimal import Decimal, ROUND_HALF_UP


class PricingRule(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    markup_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    markdown_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def applies_to_date(self, date):
        return self.start_date <= date <= self.end_date
    
class Room(models.Model):
    room_number = models.CharField(max_length=10, default='101')
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Adjusted for currency handling
    is_available = models.BooleanField(default=True)
    descriptions = models.TextField(blank=True)
    coverimage_url = models.URLField(blank=True)
    image_url2 = models.URLField(blank=True)

    def get_adjusted_price(self):
        current_date = timezone.now().date()
        active_rules = PricingRule.objects.filter(
            start_date__lte=current_date,
            end_date__gte=current_date
        )
        
        markup_percentage = Decimal('0')
        markdown_percentage = Decimal('0')

        for rule in active_rules:
            markup_percentage += Decimal(rule.markup_percentage)
            markdown_percentage += Decimal(rule.markdown_percentage)

        base_price = self.price
        adjusted_price = base_price * (Decimal('1') + (markup_percentage / Decimal('100'))) * (Decimal('1') - (markdown_percentage / Decimal('100')))
        
        # Quantize the adjusted price to 2 decimal places
        adjusted_price = adjusted_price.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        return adjusted_price
    
    def __str__(self):
        return f"{self.room_type} - {self.room_number}"
class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    booking_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking {self.booking_number} for {self.guest_name}"
    
    def save(self, *args, **kwargs):
        if not self.booking_number:
            self.booking_number = uuid.uuid4()
        super().save(*args, **kwargs)

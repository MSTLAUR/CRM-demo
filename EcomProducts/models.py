from django.db import models

# Create your models here.

class Item(models.Model):


    
    item_name = models.CharField(max_length=25)
    item_desc = models.CharField(max_length=25)
    item_price = models.IntegerField()


def __str__(self):
        return self.item_name
    
    
        
        

#create a product MODELS

class newProductModels(models.Model):
    ONE_TIME = 'one_time'
    MONTHLY = 'monthly'
    QUATERLY = 'quaterly'
    YEARLY = 'yearly'

    PAYMENT_INTERVAL_CHOICES = [
        (ONE_TIME, 'One Time'),
        (MONTHLY, 'Monthly'),
        (QUATERLY, 'Quaterly'),
        (YEARLY, 'Yearly'),
    ]

    name = models.CharField(max_length=50)
    product_ID = models.CharField(max_length=20)
    description = models.TextField()
    category = models.CharField(max_length=20)
    city = models.CharField(max_length=100, default="New york") 
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Base price per unit in dollars
    currency = models.CharField(max_length=3, default="USD")  # e.g., 'USD'
    image_url = models.URLField(blank=True, null=True)  # Optional: for displaying images in Stripe checkout
    video_link = models.URLField(blank=True, null=True)
    
    
    
    # Payment options
    payment_interval = models.CharField(
        max_length=10,
        choices=PAYMENT_INTERVAL_CHOICES,
        default=ONE_TIME,
    )
    quantity_available = models.PositiveIntegerField(default=1)  # Available stock

    # Subscription settings (if applicable)
   # trial_period_days = models.PositiveIntegerField(blank=True, null=True)  # Free trial period, if offered

    def __str__(self):
        return f'{self.name} ({self.price})'   

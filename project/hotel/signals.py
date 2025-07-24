from .models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver
from . views import customer_logged_in, customer_logged_out

@receiver(post_save, sender=Customer)
def Customer_Created(sender, instance, created, **kwargs):
    if created:
        print(f"The new Customer is created {instance.first_name} and Email Id is {instance.email}")

@receiver(customer_logged_in)
def Customer_Login(sender, customer,  **kwargs):
    print(f"Customer Login Suceess {customer.email}")

@receiver(customer_logged_out)
def Customer_Logout(sender, customer, **kwargs):
    print(f"The Customer Logout {customer.email}")
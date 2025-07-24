from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

def ageCriteria(value):
    if value<18:
        raise ValidationError("AGE Must be Greater than 18")
    
def mobileCriteria(value):
    if not value.isdigit():
        raise ValidationError("The mobile number should bre Number")
    if len(value) != 10:
        raise ValidationError("The mobile number must be 10")

def passwordCriteria(value):
    if not value.isdigit():
        raise ValidationError("The Password Should Be Digit")
    if len(value) != 6:
        raise ValidationError("The Password should be 6")   


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.IntegerField(validators=[ageCriteria])
    mobile = models.CharField(max_length=10, validators=[mobileCriteria])
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=6, validators=[passwordCriteria])

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            passwordCriteria(self.password)
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"The Customer Name is {self.first_name} and The Email is {self.email}"
    

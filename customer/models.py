from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    city_born = models.CharField(max_length=50)
    closest_friend = models.CharField(max_length=50)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    address = models.CharField(max_length=150)
    customer = models.ManyToManyField(Customer)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f'{self.address}'


class Discount(models.Model):
    discount_amount = models.IntegerField()
    discount_description = models.CharField(max_length=80)
    ACTIVE = 'active'
    DEACTIVE = 'deactive'
    choices = (
        (ACTIVE, 'active'),
   ( DEACTIVE , 'deactive')
    )
    order_status = models.CharField(max_length=30, choices=choices, db_index=True,
                                  default=ACTIVE,
                                  help_text='status of the discount')
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.discount_amount



from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
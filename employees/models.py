from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

class Employee(AbstractUser):
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name="employees",
        null=True,
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="employee_groups",
        related_query_name="employee",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="employee_permissions",
        related_query_name="employee",
    )

    def __repr__(self):
        return f"<[{self.pk}] - {self.first_name}, {self.is_superuser}>"
    
    class Meta:
        verbose_name = "User"

    def __str__(self):
        return f"{self.username} ({self.email})"

@receiver(post_save, sender=Employee)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to the company!',
            'We are glad to have you with us.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
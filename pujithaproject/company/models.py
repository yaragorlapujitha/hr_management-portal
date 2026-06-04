from datetime import timedelta

from django.utils import timezone
from django.db import models
from django.conf import settings

class Company(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    tech_stack = models.CharField(max_length=255)
    address = models.TextField()
    year_of_passing = models.PositiveIntegerField()

    added_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='companies'
    )

    created_at = models.DateTimeField(auto_now_add=True)  # set once, on insert
    updated_at = models.DateTimeField(auto_now=True)      # update on every save
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='active')
    def __str__(self):
        return f"{self.company_name} - {self.role}"

    def auto_update_status(self):
        if timezone.now() >= self.created_at + timedelta(minutes=1):
            if self.status != 'inactive':
                self.status = 'inactive'
                self.save()

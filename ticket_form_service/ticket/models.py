from django.db import models

class Ticket(models.Model):
    CATEGORY_CHOICES = [('bug', 'Bug'), ('feature', 'Feature'), ('support', 'Support')]
    PRIORITY_CHOICES = [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    contact_info = models.EmailField()

    def __str__(self):
        return self.title

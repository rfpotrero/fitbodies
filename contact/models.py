from django.db import models


class Contact(models.Model):
    """
    Model for the contact
    """
    REASON = [
        ('order', 'Order'),
        ('renting', 'Renting a Studio'),
        ('classes', 'Question about a class'),
        ('personaltrainer', 'Question about a Personal Trainer'),
        ('general', 'General enquiry'),
    ]
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    contact_reason = models.CharField(
        max_length=50,
        choices=REASON,
    )

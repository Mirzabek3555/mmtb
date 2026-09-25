from django.db import models


class Contact(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('korildi', "Ko'rildi"),
        ('javob_berildi', 'Javob berildi'),
    ]
    full_name = models.CharField("F.I.Sh.", max_length=200)
    phone = models.CharField("Telefon", max_length=50)
    email = models.EmailField("Email", blank=True)
    subject = models.CharField("Mavzu", max_length=300)
    message = models.TextField("Xabar")
    status = models.CharField("Holati", max_length=20, choices=STATUS_CHOICES, default='yangi')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

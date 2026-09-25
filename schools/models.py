from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class School(models.Model):
    TYPE_CHOICES = [
        ('maktab', 'Umumta\'lim maktabi'),
        ('maktabgacha', 'Maktabgacha ta\'lim muassasasi'),
        ('maxsus', 'Maxsus ta\'lim muassasasi'),
        ('litsey', 'Akademik litsey'),
        ('kasb', 'Kasb-hunar kolleji'),
    ]
    name = models.CharField("Maktab nomi", max_length=300)
    school_type = models.CharField("Turi", max_length=30, choices=TYPE_CHOICES, default='maktab')
    number = models.CharField("Tartib raqami", max_length=20, blank=True)
    address = models.CharField("Manzil", max_length=300)
    phone = models.CharField("Telefon", max_length=50, blank=True)
    email = models.EmailField("Email", blank=True)
    director_name = models.CharField("Direktor F.I.Sh.", max_length=200, blank=True)
    director_phone = models.CharField("Direktor telefoni", max_length=50, blank=True)
    student_count = models.PositiveIntegerField("O'quvchilar soni", default=0)
    teacher_count = models.PositiveIntegerField("O'qituvchilar soni", default=0)
    image = models.ImageField("Rasm", upload_to='schools/', blank=True, null=True)
    description = RichTextUploadingField("Tavsif", blank=True)
    founded_year = models.PositiveIntegerField("Ta'sis yili", blank=True, null=True)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ta'lim muassasasi"
        verbose_name_plural = "Ta'lim muassasalari"
        ordering = ['school_type', 'number']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('schools:detail', kwargs={'pk': self.pk})

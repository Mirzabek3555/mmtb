from django.db import models
from ckeditor.fields import RichTextField


class SiteSettings(models.Model):
    """Sayt sozlamalari"""
    organization_name = models.CharField("Tashkilot nomi", max_length=200, default="Tuproqqal'a Tuman MTB")
    organization_full_name = models.CharField("To'liq nomi", max_length=500, default="Tuproqqal'a Tuman Maktabgacha va Maktab Ta\'limi Bo\'limi")
    address = models.CharField("Manzil", max_length=300, default="Qashqadaryo viloyati, Tuproqqal'a tumani")
    phone = models.CharField("Telefon", max_length=20, default="+998 65 000-00-00")
    phone2 = models.CharField("Telefon 2", max_length=20, blank=True)
    email = models.EmailField("Email", default="info@tuproqqala-talim.uz")
    working_hours = models.CharField("Ish vaqti", max_length=100, default="Dushanba-Juma: 9:00 - 18:00")
    about_text = RichTextField("Haqida ma'lumot", blank=True)
    telegram = models.URLField("Telegram", blank=True)
    facebook = models.URLField("Facebook", blank=True)
    instagram = models.URLField("Instagram", blank=True)
    youtube = models.URLField("YouTube", blank=True)

    class Meta:
        verbose_name = "Sayt sozlamalari"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return self.organization_name


class Statistics(models.Model):
    """Statistika raqamlari"""
    title = models.CharField("Ko'rsatkich", max_length=200)
    value = models.CharField("Qiymat", max_length=50)
    icon = models.CharField("Icon (FontAwesome class)", max_length=100, default="fas fa-school")
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"
        ordering = ['order']

    def __str__(self):
        return f"{self.title}: {self.value}"


class Announcement(models.Model):
    """E'lonlar"""
    title = models.CharField("Sarlavha", max_length=300)
    content = RichTextField("Mazmuni")
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Document(models.Model):
    """Hujjatlar"""
    CATEGORY_CHOICES = [
        ('qonun', "Qonunlar va me'yoriy hujjatlar"),
        ('buyruq', "Buyruq va farmonlar"),
        ('dastur', "Ta'lim dasturlari"),
        ('hisobot', "Hisobotlar"),
        ('boshqa', "Boshqalar"),
    ]
    title = models.CharField("Nomi", max_length=300)
    file = models.FileField("Fayl", upload_to='documents/')
    category = models.CharField("Kategoriya", max_length=50, choices=CATEGORY_CHOICES, default='boshqa')
    description = models.TextField("Tavsif", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hujjat"
        verbose_name_plural = "Hujjatlar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

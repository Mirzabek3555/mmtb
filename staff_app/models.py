from django.db import models


class Department(models.Model):
    name = models.CharField("Bo'lim nomi", max_length=200)
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"
        ordering = ['order']

    def __str__(self):
        return self.name


class Staff(models.Model):
    POSITION_CHOICES = [
        ('rahbar', 'Bo\'lim boshlig\'i'),
        ('bosh_mutaxassis', 'Bosh mutaxassis'),
        ('mutaxassis', 'Mutaxassis'),
        ('inspektor', 'Inspektor'),
        ('metodist', 'Metodist'),
        ('boshqa', 'Boshqa'),
    ]
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Bo'lim")
    full_name = models.CharField("F.I.Sh.", max_length=200)
    position = models.CharField("Lavozim", max_length=100, choices=POSITION_CHOICES, default='mutaxassis')
    position_custom = models.CharField("Maxsus lavozim", max_length=200, blank=True)
    phone = models.CharField("Telefon", max_length=50, blank=True)
    email = models.EmailField("Email", blank=True)
    reception_hours = models.CharField("Qabul vaqti", max_length=200, blank=True)
    photo = models.ImageField("Foto", upload_to='staff/', blank=True, null=True)
    bio = models.TextField("Biografiya", blank=True)
    is_management = models.BooleanField("Rahbariyat", default=False)
    order = models.PositiveIntegerField("Tartib", default=0)

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

    def get_position_display_name(self):
        if self.position_custom:
            return self.position_custom
        return self.get_position_display()

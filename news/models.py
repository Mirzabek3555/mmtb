from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class NewsCategory(models.Model):
    name = models.CharField("Kategoriya", max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Yangilik kategoriyasi"
        verbose_name_plural = "Yangilik kategoriyalari"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField("Sarlavha", max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    image = models.ImageField("Rasm", upload_to='news/', blank=True, null=True)
    short_description = models.TextField("Qisqa tavsif", max_length=500)
    content = RichTextUploadingField("Mazmuni")
    is_published = models.BooleanField("Nashr etilgan", default=True)
    is_featured = models.BooleanField("Asosiy sahifada", default=False)
    views = models.PositiveIntegerField("Ko'rishlar soni", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            import uuid
            self.slug = slugify(self.title) or str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('news:detail', kwargs={'slug': self.slug})

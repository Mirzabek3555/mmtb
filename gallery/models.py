from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField("Kategoriya", max_length=100)

    class Meta:
        verbose_name = "Galereya kategoriyasi"
        verbose_name_plural = "Galereya kategoriyalari"

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kategoriya")
    title = models.CharField("Sarlavha", max_length=200)
    image = models.ImageField("Rasm", upload_to='gallery/')
    description = models.TextField("Tavsif", blank=True)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Galereya rasmi"
        verbose_name_plural = "Galereya rasmlari"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField("Nomi", max_length=200)
    youtube_url = models.URLField("YouTube havola")
    thumbnail = models.ImageField("Muqova rasmi", upload_to='videos/', blank=True, null=True)
    description = models.TextField("Tavsif", blank=True)
    is_active = models.BooleanField("Faol", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videolar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_embed_url(self):
        """YouTube embed URL'ini qaytaradi"""
        if 'watch?v=' in self.youtube_url:
            video_id = self.youtube_url.split('watch?v=')[1].split('&')[0]
        elif 'youtu.be/' in self.youtube_url:
            video_id = self.youtube_url.split('youtu.be/')[1].split('?')[0]
        else:
            return self.youtube_url
        return f"https://www.youtube.com/embed/{video_id}"

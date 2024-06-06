from django.db import models
from core.models import User
import uuid
from core.utils import *
from django.conf import settings
# Create your models here.
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

class AdminShowcase(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    @property
    def imageURL(self):
        img=''
        try:
            if self.image.url:
                img=self.image.url
        except:
            img=''

        return img
    def __str__(self):
        return self.name


class AdminLastMovies(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nota=models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    @property
    def imageURL(self):
        img=''
        try:
            if self.image.url:
                img=self.image.url
        except:
            img=''

        return img
    def __str__(self):
        return self.name
    


class AdminMovies(models.Model):
    category = models.ManyToManyField(Category, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    nota=models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.FileField(upload_to='subtitles/', blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name


    def get_vtt_subtitle_url(self):
        if self.subtitle_file:
            srt_path = self.subtitle_file.path
            print(f"Converting SRT to VTT: {srt_path}")
            vtt_path = convert_srt_to_vtt(srt_path)
            vtt_path_str = str(vtt_path)  # Convert vtt_path to string
            media_root_str = str(settings.MEDIA_ROOT)  # Convert MEDIA_ROOT to string
            vtt_url = vtt_path_str.replace(media_root_str, settings.MEDIA_URL)
            print(f"VTT URL: {vtt_url}")
            return vtt_url
        return None
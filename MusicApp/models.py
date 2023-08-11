from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as DjangoGroup


class MyMusicAppUser(AbstractUser):
    DO_NOT_SHOW = ''
    GENDERS = [
        ('male', "Male"),
        ('female', "Female"),
        (DO_NOT_SHOW, ''),
    ]

    profile_picture = models.URLField(null=True, blank=True)
    gender = models.CharField(max_length=11, choices=GENDERS, null=True, blank=True, default=DO_NOT_SHOW)


    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username


class Album(models.Model):
    CHOICES = [
        ("pop music", "Pop Music"),
        ("jazz music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Metal Music", "Metal Music"),
        ("Other", "Other"),
    ]

    album_name = models.CharField(unique=True, max_length=30)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=CHOICES)
    description = models.TextField(blank= True, null=30)
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0)])
    profile = models.ForeignKey(MyMusicAppUser, on_delete=models.CASCADE)
    average_rating = models.FloatField(null=True, blank=True)


class Review(models.Model):
    CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),

    ]

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=30)
    rating = models.CharField(choices=CHOICES, max_length=30)
    profile = models.ForeignKey(MyMusicAppUser, on_delete=models.CASCADE)


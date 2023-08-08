from django.db import models
from django.core.validators import RegexValidator, MinValueValidator


class Profile(models.Model):
    username = models.CharField(max_length=15,validators=[
            RegexValidator(
                r'^[a-zA-Z0-9_]*$',
            )
        ]
    )

    email = models.EmailField()

    age = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)


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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)



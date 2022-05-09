from django.db import models
from django.contrib.auth.models import User


# Base model for user creation and modification information
class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    modified = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        abstract = True


# Division of tasks according to the status to be completed
COLOR_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
)


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(storage='uploads/', null=True, blank=True)

    def __str__(self):
        return f'{self.user}'


class Note(BaseModel):
    user = models.ManyToManyField(UserProfile, related_name='user_note')
    title = models.CharField(max_length=100, null=False, blank=False)
    note = models.CharField(max_length=1000, null=False, blank=False)
    color = models.CharField(max_length=100, default='pending', choices=COLOR_CHOICES)

    def __str__(self):
        return f'{self.note}'

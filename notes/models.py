from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
)


# User profile based on the default django model User
class UserProfile(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            # print("create",sender, instance,created,**kwargs)
            UserProfile.objects.create(user=instance)

    def __str__(self):
        return f'{self.user}'


# Note model for application
class Note(BaseModel):
    author = models.ManyToManyField(UserProfile, related_name='author')
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    status = models.CharField(max_length=100, default='pending', choices=STATUS_CHOICES)

    def __str__(self):
        return f'{self.description}'

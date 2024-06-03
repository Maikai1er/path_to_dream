from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'CustomUser'

from django.db import models
from accounts.models import CustomUser


class Dream(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='dreams')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    time_complexity = models.IntegerField(default=0)
    effort_complexity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'dreams'


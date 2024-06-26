from django.db import models
from dreams.models import Dream


class Step(models.Model):
    dream = models.ForeignKey(Dream, on_delete=models.CASCADE, related_name='steps')
    title = models.CharField(max_length=100)
    description = models.TextField()
    minutes_needed_per_week = models.IntegerField()
    minutes_done_per_week = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'steps'

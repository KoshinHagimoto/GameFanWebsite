from django.db import models

# Create your models here.
class Player(models.Model):
    player_name = models.CharField(max_length=200)
    player_description = models.CharField(max_length=400)
    player_status = models.CharField(max_length=200)

    def __str__(self):
        return self.player_name
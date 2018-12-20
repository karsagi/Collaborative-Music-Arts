from djongo import models
from django.contrib.auth import get_user_model


# Create your models here.
class Composition(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' - ' + self.creator.username


class Variation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' (' + str(self.composition) + ') - ' + self.creator.username


class Track(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    instrument = models.CharField(max_length=100)
    composition = models.ForeignKey(Composition, on_delete=models.DO_NOTHING)
    track_file = models.FileField(upload_to='tracks')

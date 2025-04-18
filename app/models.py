from django.db import models


class PrevProj(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/')
    def __str__(self):
        return self.title
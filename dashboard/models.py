from django.db import models


class Championship(models.Model):
    name = models.CharField(max_length=100)
    registration_file = models.FileField(upload_to=f'uploads/{name}/registration_data/')
    results_file = models.FileField(upload_to=f'uploads/{name}/results_data/')

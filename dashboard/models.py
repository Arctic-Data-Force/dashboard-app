from django.db import models


def upload_to(instance, filename):
    return f'uploads/{instance.name}/{filename}'

class Championship(models.Model):
    name = models.CharField(max_length=100)
    registration_file = models.FileField(upload_to=upload_to)
    results_file = models.FileField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.name


class Competence(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "competencies"

    def __str__(self):
        return self.name

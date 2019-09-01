from django.db import models


class SkillsGroup(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = "quickstart"

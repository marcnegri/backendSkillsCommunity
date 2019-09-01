from django.db import models
from ..models.SkillsGroup import SkillsGroup
from django.contrib.auth.models import User


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=80, blank=False)
    description = models.CharField(max_length=255, blank=True)
    image_url = models.CharField(max_length=255, blank=True)
    skills_group = models.ForeignKey(SkillsGroup, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        app_label = "quickstart"

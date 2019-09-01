from django.db import models
from ..models.Skill import Skill
from django.contrib.auth.models import User
import datetime

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    reviewed_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    review_date = models.DateTimeField(default=datetime.datetime.now)
    review_grade = models.FloatField()

    class Meta:
        app_label = "quickstart"
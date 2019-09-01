from rest_framework import serializers
from ..serializers.UserSerializer import UserSerializer
from ..serializers.SkillSerializer import SkillSerializer
from ..models.Review import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'reviewed_skill', 'review_author', 'review_date', 'review_grade']

        def create(self, validated_data):
            return Review.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.review_grade = validated_data.get('review_grade', instance.label)
            instance.save()
            return instance

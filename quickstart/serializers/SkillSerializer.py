from rest_framework import serializers
from ..models.Skill import Skill
from ..serializers.UserSerializer import UserSerializer
from ..models.Review import Review

class SkillSerializer(serializers.ModelSerializer):

    global_review = serializers.SerializerMethodField()
    author = UserSerializer()

    class Meta:
        model = Skill
        fields = ['label', 'description', 'image_url', 'id', 'skills_group', 'author', 'global_review']

        def create(self, validated_data):
            return Skill.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.label = validated_data.get('label', instance.label)
            instance.description = validated_data.get('description', instance.description)
            instance.image_url = validated_data.get('image_url', instance.image_url)
            instance.save()
            return instance

    def get_global_review(self, skill):
        sum = 0
        try:
            lstReviews = Review.objects.filter(reviewed_skill_id=skill.id)
            for rv in lstReviews:
                sum = sum + rv.review_grade
            average = sum / len(lstReviews)
            return average
        except:
            return None

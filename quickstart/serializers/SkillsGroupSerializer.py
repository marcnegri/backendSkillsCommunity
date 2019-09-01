from rest_framework import serializers
from ..models.SkillsGroup import SkillsGroup

class SkillsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillsGroup
        fields = ['label', 'description', 'image_url', 'id']

        def create(self, validated_data):
            return SkillsGroup.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.label = validated_data.get('label', instance.label)
            instance.description = validated_data.get('description', instance.description)
            instance.image_url = validated_data.get('image_url', instance.image_url)
            instance.save()
            return instance

from rest_framework import serializers

from .models import Tea, TeaImages


class TeaImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeaImages
        fields = '__all__'

class TeaSerializer(serializers.ModelSerializer):
    images = TeaImagesSerializer(many=True, required=False)

    class Meta:
        model = Tea
        fields = '__all__'

from rest_framework import serializers

from posters.models import Poster


class PosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poster
        fields = '__all__'
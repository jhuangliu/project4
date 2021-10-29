from rest_framework import serializers
from .models import Poem

class PoemSerializer(serializers.HyperlinkedModelSerializer): 
  
    poem_url = serializers.ModelSerializer.serializer_url_field(
        view_name='poem_detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta: 
        model = Poem
        fields = ('id','title', 'author', 'body', 'poem_url', 'owner')

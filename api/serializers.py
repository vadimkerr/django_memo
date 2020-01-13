from rest_framework import serializers
from memo.models import Memo


class MemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memo
        fields = ['url', 'id', 'title', 'text']

from rest_framework import viewsets
from .serializers import MemoSerializer
from memo.models import Memo


class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

from rest_framework import generics  # <- import generics
from .models import Poem  # <- don't forget your models
from .serializers import PoemSerializer # <- or serializers
from rest_framework import permissions
from poems.permissions import IsOwnerOrReadOnly


class PoemList(generics.ListCreateAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PoemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    permission_classes = [IsOwnerOrReadOnly]

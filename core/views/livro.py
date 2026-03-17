from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer


class LivroViewset(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

from .models import Board_comments
from .serializers import Board_commentsSeriallizer
from rest_framework import viewsets

class Board_commentsViewSet(viewsets.ModelViewSet):
    queryset = Board_comments.objects.all()
    serializer_class = Board_commentsSeriallizer
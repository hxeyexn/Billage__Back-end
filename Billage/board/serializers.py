from .models import Board, Board_comments
from rest_framework import serializers

class Board_commentsSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Board_comments
        fields = '__all__'
        # exclude = ('board_id', 'comment_id',) 
        # 댓글 작성시 board_id, comment_id(ForeignKey)가 보이지 않음
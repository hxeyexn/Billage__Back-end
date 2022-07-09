from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150,verbose_name='글 제목')
    description = models.TextField(verbose_name='글 내용')
    image = models.CharField(max_length=300)
    writer = models.ForeignKey('accounts.User',related_name='board',on_delete=models.CASCADE,verbose_name='작성자',db_column="writer")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='글 작성 시간')

    def __str__(self):
        return self.title

class BoardInfo(models.Model):
    id = models.AutoField(primary_key=True)
    board_id = models.ForeignKey(Board,related_name="boardinfo", on_delete=models.CASCADE, db_column="board_id")
    category = models.CharField(max_length=20,verbose_name="분류")
    price = models.CharField(max_length=20,verbose_name="가격")
    process_status = models.CharField(max_length=20,verbose_name="상태")  

class Board_comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    board_id = models.ForeignKey("Board", related_name="comment", on_delete=models.CASCADE, db_column="board_id")
    content = models.TextField(blank=False)
    create_time = models.DateTimeField(auto_now_add=True) 
    writer = models.ForeignKey("accounts.User",  related_name="writers", on_delete=models.CASCADE)
    comment_id = models.ForeignKey("Board_comments", related_name="reply", on_delete=models.CASCADE, db_column="comment_id", null=True, blank=True)


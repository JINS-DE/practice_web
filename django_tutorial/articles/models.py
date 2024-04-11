from django.db import models

class Article(models.Model): #상속
    # id는 자동으로 만들어진다
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
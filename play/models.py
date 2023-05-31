from django.db import models
import markdown

# Create your models here.
class Mission(models.Model):
    key = models.CharField(max_length=100)
    chapter = models.CharField(max_length=100, default='blank')
    content = models.TextField()
    w3w = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    next = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.key}, {self.w3w}"
    
    def html(self):
        return markdown.markdown(self.content, extensions=['fenced_code'])
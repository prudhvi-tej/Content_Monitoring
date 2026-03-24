from django.db import models

class Keyword(models.Model):
    name = models.CharField(max_length=255)

class ContentItem(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    source = models.CharField(max_length=100)
    last_updated = models.DateTimeField()

class Flag(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    content_item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    score = models.IntegerField()
    status = models.CharField(max_length=20, default='pending')
    reviewed_at = models.DateTimeField(null=True, blank=True)

def __str__(self):
    return self.name
from django.db import models

class Topic(models.Model):
    tweet_id = models.CharField(max_length=19, blank=False, null=False)
    text = models.CharField(max_length=300, null = False)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    url = models.CharField(max_length=150, blank=True, null=False)
    first_tweet = models.IntegerField(default = 0)
    topic_id = models.IntegerField(default= 0, null=False)
    def __str__(self):
        return self.text

    

# Create your models here.

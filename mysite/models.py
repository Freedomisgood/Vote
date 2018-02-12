from django.db import models
# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=200,null=False)
    created_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PollItem(models.Model):
    poll = models.ForeignKey(Poll,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False)
    image_url = models.CharField(max_length=200,null=False,blank=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
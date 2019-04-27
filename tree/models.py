from django.db import models

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=200)
	picture_url = models.TextField(blank=True, null=True)
	parent = models.ForeignKey('self', null=True, blank=True,  on_delete=models.CASCADE)
	order = models.IntegerField(default=0)	
	def __str__(self):
		return self.name

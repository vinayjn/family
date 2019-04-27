from django.db import models

# Create your models here.
class Member(models.Model):
	name = models.CharField(max_length=200)
	picture_url = models.TextField(null=True)
	parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

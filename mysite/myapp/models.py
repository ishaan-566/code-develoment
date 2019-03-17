from django.db import models

class Attribute(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def number(self):
        q1 = SubAttribute.objects.filter(attribute = self).count()
        return q1

class SubAttribute(models.Model):
    name = models.CharField(max_length=30)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    

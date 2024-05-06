from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = '"Course"'

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    note = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


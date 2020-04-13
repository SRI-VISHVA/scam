from django.db import models


class PhoneForm(models.Model):
    email = models.EmailField()
    subjects = models.TextField()
    messages = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


from django.db import models
from auth_manage.models import Users

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to= 'files/')
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} - {self.file.name}"
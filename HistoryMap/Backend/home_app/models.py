from django.db import models
from usermanage_app.models import Users

# Create your models here.
class Stories(models.Model):
    history_name = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    latitud = models.FloatField()
    longitud = models.FloatField()
    user_name = models.ForeignKey(Users, on_delete= models.CASCADE, related_name='stories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.history_name

class Reaction(models.Model):

    REACTION_TYPES = [
        ('like', 'Me gusta'),
        ('love', 'Me encanta'),
        ('wow', 'Wow'),
    ]

    tipo = models.CharField(max_length=20, choices=REACTION_TYPES)
    user_name = models.ForeignKey(Users, on_delete= models.CASCADE, related_name='reactions_given')
    history_name = models.ForeignKey(Stories, on_delete= models.CASCADE, related_name='reactions')
    created_at = models.DateField()

class Comment(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comments' )
    history_name = models.ForeignKey(Stories, on_delete= models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.story.history_name}'

class Share(models.Model):
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='shares_given' )
    history_name = models.ForeignKey(Stories, on_delete= models.CASCADE, related_name='shares')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Shared by {self.user.username} on {self.story.history_name}'
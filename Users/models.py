from django.db import models
from PIL import Image
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='PROFILE-PICS')
    def __str__(self):
        return f'{self.user.username} PROFILE'
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class FollowList(models.Model):
    usr=models.ForeignKey(User,related_name='yuser',on_delete=models.CASCADE)
    followings=models.ManyToManyField(User,related_name='followings')
    def __str__(self):
        return str(self.usr)
    


from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# setting up pfofile picture
# settig one to one relationship between user and user profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    # example to overwrite the default save method for the model

    # def save(self,force_insert=False):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size =(300, 300)
    #         img.trumbnail(output_size)
    #         img.save(self.image.path)


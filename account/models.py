import os
import datetime
from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, filename):
    dir_name = datetime.datetime.now().strftime("profile/%Y/")
    return os.path.join(dir_name + str(instance.id), filename)

# def generate_file(self, instance, filename):
#     if callable(self.upload_to):
#         filename = self.upload_to(instance, filename)
#         filename = dateti


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True, upload_to=get_image_path)

    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.photo
            self.photo = None
            super(Profile, self).save(*args, **kwargs)
            self.photo = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
            

        super(Profile, self).save(*args, **kwargs)

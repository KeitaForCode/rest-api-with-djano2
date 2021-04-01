from django.conf import settings
from django.db import models

def upload_update_image(instance, filename):
    """this will set the path for the upload images"""
    return "updates/{users}/{filename}".format(user=instance.user, filename=filename)


class Update(models.Model):
    """This will create the model for update"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """this will return the string representation of the updates model"""
        return self.content or ""

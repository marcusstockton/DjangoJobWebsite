from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return '{0}/{1}'.format(instance.User.username, filename)


class Attachment(models.Model):
    avatar = models.ImageField(upload_to=upload_location, null=True, blank=True)
    cv = models.FileField(upload_to=upload_location, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("attachments:detail", kwargs={"pk": self.id})




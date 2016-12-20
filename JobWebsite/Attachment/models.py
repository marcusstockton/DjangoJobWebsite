import os
import tempfile
import base64

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.models.functions import datetime


class Attachment(models.Model):
    file_name = models.CharField(max_length=120)
    data = models.BinaryField()
    created_date = models.DateField(auto_now_add=True)
    file_type = models.CharField(max_length=120)
    active = models.BooleanField()
    User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name

    def get_absolute_url(self):
        return reverse("attachments:detail", kwargs = { "pk": self.id })


def handle_uploaded_file(instance, file):
    tup = tempfile.mkstemp()  # make a tmp file
    f = os.fdopen(tup[0], 'w')  # open the tmp file for writing
    f.write(str(file.read()))  # write the tmp file
    f.close()

    # return the path of the file
    filepath = tup[1]  # get the filepath
    with open(filepath, 'rb') as f:
        encoded = f.read()
        b64 = base64.encodebytes(encoded) # fuck knows what needs saving, its not this hard in .net
        filename = filepath
        extension = file.content_type


    saved_data = Attachment(file_name=filename, data=b64, created_date=datetime.datetime.now(),
                            file_type=extension, active=True, User=instance)

    saved_data.save(force_insert=True)
    return saved_data.file_name

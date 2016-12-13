mstockton
P@ssword


Notes for me:
have Jobs working in so far as index, details and edit pages go.


test@test.com
P@ssword

In company views, the edit page now adds in widgets, but I need to wire up Instance so it loads data to the form.
Also need to actually save the data.

TODO:
Create a string list of years for the User Edit form.
Fix up the format the date is passed in for date of birth in User edit form

The following is how to create related objects. This has been tested in python shell

from Attachment.models import Attachment
from User.models import User
nathan = User.objects.create(username='nathan', first_name="nathan", last_name="sykes", email="nat@han.com", password="1234")
nathan.attachment_set.create(file_name="test.txt", data=bytearray(10), created_date="13/12/2016", file_type="txt", active=True)

Need to implement this in the code, reading out the inmemoryuploadedfile to disk...somehow.
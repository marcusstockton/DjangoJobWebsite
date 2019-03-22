import django_tables2 as tables
from django_tables2.utils import A
from django.utils.html import format_html

from .models import User

class ImageColumn(tables.Column):
    def render(self, value):
        if value:
            return format_html('<img src="{}" height="120px"/>', value.avatar.url)

class UserTable(tables.Table):
    view = tables.LinkColumn('users:detail', text='View', args=[A('pk')], orderable=False)
    edit = tables.LinkColumn('users:edit', text='Edit', args=[A('pk')], orderable=False)
    attachment = ImageColumn()

    class Meta:
        model = User
        exclude = ['id', 'password']


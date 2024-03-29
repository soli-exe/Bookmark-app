from django.db import models
from django.db.models.fields import (CharField,
                                     URLField)


class BookMark(models.Model):
    bookmark_title = CharField(
        max_length=250, null=False, blank=False)
    bookmark_link = URLField(null=False, blank=False)
    owner = models.ForeignKey('accounts.CustomUser',
                              on_delete=models.CASCADE,
                              null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self) -> str:
        return self.bookmark_title

from django.db import models
from django.db.models.fields import CharField, URLField


class DemoBookMark(models.Model):
    bookmark_title_demo = CharField(
        max_length=250, null=False, blank=False)
    bookmark_link_demo = URLField(null=False, blank=False)
    publication_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.bookmark_title_demo

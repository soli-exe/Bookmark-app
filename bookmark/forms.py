from .models import BookMark
from bootstrap_modal_forms.forms import BSModalModelForm


class BookmarkModelForm(BSModalModelForm):
    class Meta:
        model = BookMark
        exclude = ['timestamp']

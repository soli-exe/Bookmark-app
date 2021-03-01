from bootstrap_modal_forms.forms import BSModalModelForm
from .models import DemoBookMark


class BookmarkDemoModelForm(BSModalModelForm):
    class Meta:
        model = DemoBookMark
        fields = ['bookmark_title_demo', 'bookmark_link_demo']
        exclude = ['publication_date']

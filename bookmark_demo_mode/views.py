from django.db.models.fields import FloatField
from django.views.generic import ListView
from .models import DemoBookMark
from django.urls import reverse_lazy
from .forms import BookmarkDemoModelForm
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalDeleteView)


class DemoIndex(ListView):
    model = DemoBookMark
    context_object_name = 'demo_bookmarks'
    template_name = 'demo_templates/index_demo.html'


class DemoBookmarkAddView(BSModalCreateView):
    form_class = BookmarkDemoModelForm
    template_name = 'demo_templates/bookmark_demo_add.html'
    success_message = 'Bookmark Added.'
    success_url = reverse_lazy('bookmark_demo_mode:demo_index')


class DemoBookmarkUpdateView(BSModalUpdateView):
    model = DemoBookMark
    template_name = 'demo_templates/bookmark_demo_edit.html'
    form_class = BookmarkDemoModelForm
    success_message = 'Bookmark Updated.'
    success_url = reverse_lazy('bookmark_demo_mode:demo_index')


class DemoBookmarkDeleteView(BSModalDeleteView):
    model = DemoBookMark
    template_name = 'demo_templates/bookmark_demo_delete.html'
    success_message = 'Bookmark has been Removed!'
    success_url = reverse_lazy('bookmark_demo_mode:demo_index')

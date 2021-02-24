from django.shortcuts import render
from django.views import generic
from .models import BookMark
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalDeleteView, BSModalLoginView,
                                           BSModalUpdateView)
from .forms import (BookmarkModelForm, CustomAuthenticationForm)


def search(request):
    if request.method == "GET":
        search = request.GET.get('search')
        bookmarks = BookMark.objects.all().filter(bookmark_title=search)
        return render(request, 'search_bar.html', {'bookmarks': bookmarks})


class BookmarkListView(generic.ListView):
    model = BookMark
    context_object_name = 'bookmarks'
    template_name = 'index.html'


class BookCreateView(BSModalCreateView):
    template_name = 'add_book.html'
    form_class = BookmarkModelForm
    success_message = 'Bookmark Added.'
    success_url = reverse_lazy('index')


class BookmarkUpdateView(BSModalUpdateView):
    model = BookMark
    template_name = 'bookmark_edit.html'
    form_class = BookmarkModelForm
    success_message = 'Bookmark Edited.'
    success_url = reverse_lazy('index')


class BookmarkDeleteView(BSModalDeleteView):
    model = BookMark
    template_name = 'bookmark_delete.html'
    context_object_name = 'bookmarks'
    success_message = 'Bookmark Deleted!'
    success_url = reverse_lazy('index')


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    success_message = 'Welcome'
    extra_context = dict(success_url=reverse_lazy('index'))

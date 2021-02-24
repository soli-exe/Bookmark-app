from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin,)
from django.db.models import Q
from django.http.response import HttpResponse
from django.views import generic
from .models import BookMark
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalDeleteView, BSModalLoginView,
                                           BSModalUpdateView)
from .forms import (BookmarkModelForm, CustomAuthenticationForm)


class SearchView(generic.ListView):
    model = BookMark
    template_name = 'search_result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = BookMark.objects.filter(
            Q(bookmark_title__icontains=query)
        )
        return object_list


class BookmarkListView(generic.ListView):
    model = BookMark
    context_object_name = 'bookmarks'
    template_name = 'index.html'


class BookCreateView(LoginRequiredMixin,
                     BSModalCreateView):
    template_name = 'add_book.html'
    form_class = BookmarkModelForm
    success_message = 'Bookmark Added.'
    success_url = reverse_lazy('index')

    def form_valid(self, form) -> HttpResponse:
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkUpdateView(LoginRequiredMixin,
                         UserPassesTestMixin,
                         BSModalUpdateView):
    model = BookMark
    template_name = 'bookmark_edit.html'
    form_class = BookmarkModelForm
    success_message = 'Bookmark Edited.'
    success_url = reverse_lazy('index')

    def test_func(self):
        objects = self.get_object()
        return objects.owner == self.request.user


class BookmarkDeleteView(LoginRequiredMixin,
                         UserPassesTestMixin,
                         BSModalDeleteView):
    model = BookMark
    template_name = 'bookmark_delete.html'
    context_object_name = 'bookmarks'
    success_message = 'Bookmark Deleted!'
    success_url = reverse_lazy('index')

    def test_func(self):
        objects = self.get_object()
        return objects.owner == self.request.user


class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    success_message = 'Welcome'
    extra_context = dict(success_url=reverse_lazy('index'))

from django.urls import reverse, reverse_lazy

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView
from memo.models import Memo


class IndexView(TemplateView):
    template_name = "memo/index.html"


class CreateMemoView(CreateView):
    model = Memo
    template_name = "memo/create.html"
    success_url = reverse_lazy("memo:list")
    fields = ["title", "text"]

    def get_form(self, form_class=None):
        form = super(CreateMemoView, self).get_form(form_class)
        form.label_suffix = ""
        return form


class ListMemoView(ListView):
    model = Memo
    template_name = "memo/list.html"
    context_object_name = "memos"


class DetailMemoView(DetailView):
    model = Memo
    template_name = "memo/detail.html"
    context_object_name = "memo"


class DeleteMemoView(DeleteView):
    model = Memo
    template_name = "memo/delete.html"
    success_url = reverse_lazy("memo:list")
    context_object_name = "memo"


class UpdateMemoView(UpdateView):
    model = Memo
    template_name = "memo/update.html"
    fields = ["title", "text"]

    def get_form(self, form_class=None):
        form = super(UpdateMemoView, self).get_form(form_class)
        form.label_suffix = ""
        return form

    def get_success_url(self):
        return reverse("memo:detail", kwargs={'pk': self.object.pk})

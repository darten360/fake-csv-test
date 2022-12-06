from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from fake_csv.forms import SchemaForm, FieldsForm
from fake_csv.models import Schema


@login_required
def index(request):
    """View function for the home page of the site."""

    return render(request, "fake_csv/index.html")


def login_view(request):
    if request.method == "GET":
        return render(request, "registration/login.html")

    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("fake_csv:schema_list"))
        else:
            error_context = {
                "errors": "Invalid credationals"
            }

            return render(request, "registration/login.html", context=error_context)


@login_required
def logged_out_view(request):
    logout(request)

    return render(request, "registration/logged_out.html")


@login_required
def schema_create_view(request):
    form = SchemaForm(request.POST or None)
    flds = FieldsForm(request.POST or None)
    if form.is_valid():
        form.save()

    if request.method == "GET":
        context = {
            "flds": flds,
            "form": form
        }

        return render(request, "fake_csv/schema_form.html", context=context)

    elif request.method == "POST":
        context = {
            "flds": flds,
            "form": form
        }

        return render(request, "fake_csv/schema_form.html", context=context)

    # def get_success_url(self):
    #     return reverse("fake_csv:schema_detail", kwargs={"pk": self.object.pk})


class SchemaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Schema

    def get_success_url(self):
        return reverse("fake_csv:schema_detail", kwargs={"pk": self.object.pk})


class SchemaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Schema
    template_name = "fake_csv/schema_detail.html"


class SchemaListView(LoginRequiredMixin, generic.ListView):
    model = Schema
    template_name = "fake_csv/schema_list.html"
    paginate_by = 3


class SchemaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Schema
    template_name = "fake_csv/schema_delete.html"
    success_url = reverse_lazy("fake_csv:schema_list")

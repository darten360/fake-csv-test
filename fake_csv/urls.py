from django.urls import path

from fake_csv.views import *

urlpatterns = [
    path("", index, name="home_page"),
    path("login/", login_view, name="login"),
    path("logged_out/", logged_out_view, name="logged_out"),
    path("schemas/create/", schema_create_view, name="schema_create"),
    path("schemas/update/<int:pk>", SchemaUpdateView.as_view(), name="schema_update"),
    path("schemas/delete/<int:pk>", SchemaDeleteView.as_view(), name="schema_delete"),
    path("schemas/<int:pk>", SchemaDetailView.as_view(), name="schema_detail"),
    path("schemas/", SchemaListView.as_view(), name="schema_list"),
]

app_name = "fake_csv"

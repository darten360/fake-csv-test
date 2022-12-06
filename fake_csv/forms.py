from django import forms

from fake_csv.models import Schema


def get_model_fields(model):
    my_model_fields = [field.name for field in model._meta.get_fields()]
    fields_choices = [(i, i.capitalize().replace("_", "") if "_" in i else i.capitalize) for i in my_model_fields[1:]]
    return fields_choices


class SchemaParentForm(forms.ModelForm):
    COMMA = ","
    POINT = "."
    SEMICOLON = ";"
    HORIZONTAL_TAB = r"\t"
    COLON = ":"

    SEPARATOR_CHOICES = [
        (COMMA, "Comma (,)"),
        (POINT, "Point (.)"),
        (SEMICOLON, "Semicolon (;)"),
        (HORIZONTAL_TAB, r"Horizontal tab (\t)"),
        (COLON, "Colon (:)")
    ]

    DOUBLE_QUOTES = '""'
    SINGLE_QUOTES = "''"

    QUOTES_CHOICES = [
        (DOUBLE_QUOTES, 'Double quotes (")'),
        (SINGLE_QUOTES, "Single quotes (')")
    ]
    FIELDS_CHOICES = get_model_fields(Schema)

    separator = forms.CharField(widget=forms.Select(choices=SEPARATOR_CHOICES))
    string = forms.CharField(widget=forms.Select(choices=QUOTES_CHOICES))
    field_types = forms.CharField(widget=forms.Select(choices=FIELDS_CHOICES))

    class Meta:
        model = Schema
        fields = ["name", "separator", "string"]


class FieldsForm(SchemaParentForm):
    def __init__(self, *args, **kwargs):
        super(FieldsForm, self).__init__(*args, **kwargs)
        self.fields.pop('name')
        self.fields.pop('separator')
        self.fields.pop('string')


class SchemaForm(SchemaParentForm):
    def __init__(self, *args, **kwargs):
        super(SchemaForm, self).__init__(*args, **kwargs)
        self.fields.pop("field_types")

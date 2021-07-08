from django import forms

class DocumentoForm(forms.Form):
    file = forms.FileField(label="Selecciona un archivo", help_text="Max. 42 megabytes")
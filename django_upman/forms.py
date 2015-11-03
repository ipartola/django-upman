from __future__ import unicode_literals, print_function, absolute_import, division

from django import forms


class UploadForm(forms.Form):
    file = forms.FileField()


class ImageUploadForm(forms.Form):
    file = forms.ImageField()


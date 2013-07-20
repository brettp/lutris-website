from django import forms
from common import models


class NewsForm(forms.ModelForm):
    # pylint: disable=W0232, R0903
    class Meta:
        model = models.News
        exclude = ('slug', )

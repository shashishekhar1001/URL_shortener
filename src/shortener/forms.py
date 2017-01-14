from django import forms
from .validators import validate_url, dot_com_validator

class SubmitUrlForm(forms.Form):
    url = forms.CharField(label = "Submit URL", validators=[validate_url, dot_com_validator])

    #Generic clean method for all form fields
    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data.get("url")
    #     print("From Generic clean :- {0}".format(url))

    #url field specific clean method
    # def clean_url(self):
    #     url = self.cleaned_data.get("url")
    #     print("From URL clean :- {0}".format(url))
    #     return url
        
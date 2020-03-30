from django import forms


class DMail(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email

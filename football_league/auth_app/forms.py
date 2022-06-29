from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(
        label='inputUsername',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )

    password = forms.CharField(
        label='inputPassword',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )
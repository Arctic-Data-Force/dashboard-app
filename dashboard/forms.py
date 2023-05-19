from django import forms


class ChampionshipForm(forms.Form):
    name = forms.CharField(max_length=100)
    registration_file = forms.FileField()
    results_file = forms.FileField(required=False)

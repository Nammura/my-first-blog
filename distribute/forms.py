from django import forms




class DistributeForm(forms.Form):
    distText = forms.CharField(
        label='',
        max_length=200,
        widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))
    
    
class PlayerForm(forms.Form):
        player = forms.MultipleChoiceField(
        label = "",
        required = True,
        disabled = False,
        widget = forms.CheckboxSelectMultiple(attrs={'id': 'player','class': 'form-checker-input'}))



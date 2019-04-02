from django import forms

class RouteForm(forms.Form):
    route_number=forms.IntegerField()

class StartForm(forms.Form):
    start_name=forms.CharField()

class CostForm(forms.Form):
    cost_amount=forms.IntegerField()

import datetime
from django import forms
from django.core import validators

from .services.assist_trip_service import AssistTripService


def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


# TODO: check how the form is validated to bypass problem with dates in the past
class SearchForm(forms.Form):
    destination_list = AssistTripService.get_destinations()
    destinations = forms.ChoiceField(choices=[('0', '--Selecione--')] +
                                             [(destination.id, destination.name) for destination in destination_list],
                                     label='Destino', required=True)
    boarding = forms.DateField(widget=forms.SelectDateWidget(), label='Data do Embarque', required=True,
                               validators=[present_or_future_date])
    landing = forms.DateField(widget=forms.SelectDateWidget(), label='Data do Embarque', required=True,
                              validators=[present_or_future_date])
    email = forms.EmailField(widget=forms.EmailInput(), validators=[validators.EmailValidator], required=True)



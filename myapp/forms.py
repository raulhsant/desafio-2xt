import datetime
from django import forms

from .services.assist_trip_service import AssistTripService


def present_or_future_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value


# TODO: check how the form is validated to bypass problem with dates in the past
class SearchForm(forms.Form):
    destination_list = AssistTripService.get_destinations()
    selected_destination = forms.ChoiceField(choices=[(destination.id, destination.name)
                                              for destination in sorted(destination_list, key=lambda dest: dest.id)
                                              ], label='Destino', required=True)

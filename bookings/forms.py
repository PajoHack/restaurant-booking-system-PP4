from .models import Restaurant, Table, Booking
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from django import forms
from .models import Booking, Restaurant, Table
from django.core.exceptions import ValidationError
from django.utils import timezone

class BookingForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'id': 'date'})
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'timepicker', 'id': 'time-input'}, format='%H:%M'), 
        input_formats=['%H:%M']
    )
    tables = forms.ModelMultipleChoiceField(
        queryset=Table.objects.all(), widget=forms.CheckboxSelectMultiple(
            attrs={'id': 'tables'}))
    guests = forms.IntegerField(
        min_value=1, max_value=14, widget=forms.NumberInput(
            attrs={'id': 'guests'}))
    restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(), widget=forms.HiddenInput(), required=False, label='')
    user_name = forms.CharField(max_length=200) 
    user_phone = forms.CharField(max_length=15)  

    class Meta:
        model = Booking
        fields = ['date', 'time', 'tables', 'guests', 'user_name', 'user_phone'] 

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.localdate():
            raise ValidationError('Past dates cannot be chosen.')
        return date

    def clean_time(self):
        time = self.cleaned_data.get('time')
        if time:
            if time.hour < 12 or (time.hour > 21 or (time.hour == 21 and time.minute > 30)):
                raise ValidationError('Bookings can only be made between 12 midday and 9:30 pm.')
        return time

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        try:
            self.fields['restaurant'].initial = Restaurant.objects.get(name='DeAngelos')
        except Restaurant.DoesNotExist:
            pass
        self.fields['restaurant'].widget = forms.HiddenInput()




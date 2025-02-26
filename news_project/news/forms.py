from django import forms
from django.contrib.gis.geos import Point
from leaflet.forms.widgets import LeafletWidget

from .models import Landmark


# class LandmarkForm(forms.ModelForm):
#     latitude = forms.FloatField(required=False, label='Latitude')
#     longitude = forms.FloatField(required=False, label='Longitude')

#     class Meta:
#         model = Landmark
#         fields = ['name', 'latitude', 'longitude', 'location']  # Добавляем location для редактирования
#         widgets = {
#             'location': LeafletWidget(attrs={'height': 400, 'width': 600}),  # Применяем виджет только к location
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         latitude = cleaned_data.get('latitude')
#         longitude = cleaned_data.get('longitude')

#         if latitude is not None and longitude is not None:
#             cleaned_data['location'] = Point(longitude, latitude)

#         return cleaned_data


class LandmarkForm(forms.ModelForm):
    latitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False, widget=forms.HiddenInput())
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False, widget=forms.HiddenInput())

    class Meta:
        model = Landmark
        fields = ['name', 'latitude', 'longitude', 'location']
        widgets = {
            'location': LeafletWidget(attrs={'height': 400, 'width': 600}),
        }

    def clean(self):
        cleaned_data = super().clean()
        lat = cleaned_data.get('latitude')
        lng = cleaned_data.get('longitude')

        if lat and lng:
            cleaned_data['location'] = Point(float(lng), float(lat))  # Сохраняем объект Point

        return cleaned_data




# class LandmarkForm(forms.ModelForm):
#     latitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False)  # Широта
#     longitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False)  # Долгота

#     class Meta:
#         model = Landmark
#         fields = ['name', 'latitude', 'longitude', 'location']  # Только поле location
#         widgets = {
#             'location': LeafletWidget(attrs={'height': 400, 'width': 600}),
#         }

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         if self.cleaned_data.get('latitude') and self.cleaned_data.get('longitude'):
#             # Если были изменены широта и долгота, обновляем объект location
#             instance.location = Point(self.cleaned_data['longitude'], self.cleaned_data['latitude'])
#         if commit:
#             instance.save()
#         return instance
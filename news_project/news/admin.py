from django import forms
from django.contrib import admin
from django.contrib.gis.geos import Point
from django_summernote.admin import SummernoteModelAdmin
from leaflet.admin import LeafletGeoAdmin

from .forms import LandmarkForm, LeafletWidget
# admin.py
from .models import Landmark, News
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(News, NewsAdmin)

# class LandmarkAdmin(LeafletGeoAdmin):
#     form = LandmarkForm
#     list_display = ('name', 'rating')  # Отображаем только имя и рейтинг в списке
#     readonly_fields = ('location',)  # Только поле location, так как latitude и longitude — это свойства

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'location':
#             kwargs['widget'] = LeafletWidget  # Используем класс виджета, а не экземпляр
#         return super().formfield_for_dbfield(db_field, **kwargs)

#     def save_model(self, request, obj, form, change):
#         # Обновляем location при изменении latitude и longitude
#         if 'latitude' in form.changed_data or 'longitude' in form.changed_data:
#             obj.location = Point(obj.longitude, obj.latitude)
#         super().save_model(request, obj, form, change)

# admin.site.register(Landmark, LandmarkAdmin)

class LandmarkAdmin(LeafletGeoAdmin):
    form = LandmarkForm
    list_display = ('name', 'latitude', 'longitude', 'rating')
    readonly_fields = ('latitude', 'longitude')
    class Media:
        js = ('admin/js/landmark_sync.js',) 
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'location':
            kwargs['widget'] = LeafletWidget  # Используем класс виджета, а не экземпляр
        return super().formfield_for_dbfield(db_field, **kwargs)
    def save_model(self, request, obj, form, change):
        # Обновляем координаты location перед сохранением
        if 'latitude' in form.changed_data or 'longitude' in form.changed_data:
            obj.location = Point(obj.longitude, obj.latitude)
        super().save_model(request, obj, form, change)
admin.site.register(Landmark)

import os
from django.contrib.gis.db import models
# models.py
from django.contrib.auth import get_user_model
from PIL import Image
from django.contrib.gis.geos import Point

User = get_user_model()

class News(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='main_images/')  # сохраняем в папку main_images
    preview_image = models.ImageField(upload_to='previews/', blank=True, null=True)  # сохраняем в папку previews
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала сохраняем объект

        if self.main_image:  # если есть главное изображение
            img = Image.open(self.main_image.path)  # открываем главное изображение
            img.thumbnail((200, 200))  # уменьшаем до 200px по наименьшей стороне
            
            preview_path = os.path.join('media', 'previews', os.path.basename(self.main_image.name))

            img.save(preview_path)  # сохраняем уменьшенное изображение в папку previews

            self.preview_image = os.path.relpath(preview_path, 'media')  # сохраняем относительный путь к превью
            super().save(update_fields=['preview_image'])  # обновляем только поле preview_image
    def __str__(self):
        return self.title
    
# class Landmark(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.PointField(default=Point(0, 0))  # Это поле будет хранить и широту, и долготу
#     rating = models.IntegerField()

#     @property
#     def latitude(self):
#         return self.location.y if self.location else None

#     @latitude.setter
#     def latitude(self, value):
#         if self.location:
#             self.location.y = value
#         else:
#             self.location = Point(self.longitude, value)

#     @property
#     def longitude(self):
#         return self.location.x if self.location else None

#     @longitude.setter
#     def longitude(self, value):
#         if self.location:
#             self.location.x = value
#         else:
#             self.location = Point(value, self.latitude)

#     def __str__(self):
#         return self.name
    



class Landmark(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField(default=Point(0, 0))  
    rating = models.IntegerField()

    latitude = models.FloatField(null=True, blank=True)  # Теперь это реальные поля
    longitude = models.FloatField(null=True, blank=True)  

    def save(self, *args, **kwargs):
        # Если широта и долгота заданы, обновляем location
        if self.latitude is not None and self.longitude is not None:
            self.location = Point(self.longitude, self.latitude)
        else:
            # Если location уже установлен, вытаскиваем широту и долготу
            if self.location:
                self.latitude = self.location.y
                self.longitude = self.location.x
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# class Landmark(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.PointField(default=Point(0, 0))  # Это поле будет хранить и широту, и долготу
#     rating = models.IntegerField()

# # 
#     latitude = models.FloatField(null=True, blank=True)
#     longitude = models.FloatField(null=True, blank=True)
# # 
#     @property
#     def latitude(self):
#         return self.location.y if self.location else None

#     @property
#     def longitude(self):
#         return self.location.x if self.location else None

#     def __str__(self):
#         return self.name

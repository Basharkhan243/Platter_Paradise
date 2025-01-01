from django.contrib import admin
from .models import ImageData
from .models import SearchQuery
# Register your models here.

admin.site.register(ImageData)
admin.site.register(SearchQuery)

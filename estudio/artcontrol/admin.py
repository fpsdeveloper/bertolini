from django.contrib import admin

# Register your models here.
from .models import (
        estudio,art,juzgado
        )

admin.site.register(estudio)
admin.site.register(art)
admin.site.register(juzgado)

from django.contrib import admin
from . import models

admin.site.register(models.workmodel)
admin.site.register(models.Parties)
admin.site.register(models.ProgramType)
admin.site.register(models.Programs)
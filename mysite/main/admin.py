from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = [
    #     "title",
    #     "published",
    #     "content"
    # ]
    fieldsets = [
        ("Title/Date",{"fields":["title","published"]}),
        ("URL",{"fields":["slug"]}),
        ("Series",{"fields":["series"]}),
        ("Content",{"fields":["content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)
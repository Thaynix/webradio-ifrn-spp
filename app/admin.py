from django.contrib import admin
from .models import Program, WarningCard, ProfileCard, ImageCarousel, AboutRadio


# Register your models here.
admin.site.register(Program)
admin.site.register(WarningCard)
admin.site.register(ProfileCard)
admin.site.register(ImageCarousel)
admin.site.register(AboutRadio)


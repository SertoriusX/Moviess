from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(AdminProfile)
admin.site.register(Category)
admin.site.register(AdminShowcase)
admin.site.register(AdminLastMovies)
admin.site.register(AdminMovies)


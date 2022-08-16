from django.contrib import admin
from .models import rent
from .models import user

admin.site.register(rent)
admin.site.register(user)
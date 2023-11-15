from django.contrib import admin
from .models import User, WasteCollector, WasteRecycler
admin.site.register(User)
admin.site.register(WasteCollector)
admin.site.register(WasteRecycler)


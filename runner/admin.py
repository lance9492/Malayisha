from django.contrib import admin
from .models import Runner, RunnerService, ErrandRequest

admin.site.register(Runner)
admin.site.register(RunnerService)
admin.site.register(ErrandRequest)
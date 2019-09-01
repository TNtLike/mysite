from django.contrib import admin
from .models import psn
from .models import ent
from .models import psn_resume
from .models import ent_jobs
# Register your models here.
admin.site.register(psn)
admin.site.register(ent)
admin.site.register(psn_resume)
admin.site.register(ent_jobs)

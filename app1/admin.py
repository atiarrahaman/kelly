from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(AboutContent)

@admin.register(Skill) 
class SkillAdmin(admin.ModelAdmin):
    list_display=['name','percent','value']

admin.site.register(Countup)
admin.site.register(Testimonial)
admin.site.register(Education)
admin.site.register(Summary)
admin.site.register(ProfesionalExperience)
admin.site.register(ServicePart)
admin.site.register(Map)


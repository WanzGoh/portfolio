from django.contrib import admin
from .models import Resume,Skill,Project

# Register your models here.
admin.site.register(Project)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title','date','position', 'content')

admin.site.register(Resume, ResumeAdmin)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')

admin.site.register(Skill, SkillAdmin)

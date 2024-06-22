from django.contrib import admin
from .models import Project , Skill , Message , Account



@admin.register(Project) 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name' , 'demo' , 'github' , 'video']
    search_fields = ['name']
    list_editable = ['demo' , 'github' , 'video']
    prepopulated_fields = {'slug' : ('name',)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin) : 
    list_display = ['name']
    search_fields = ['name'] 


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['email' , 'subject' , 'created_at' , 'is_readed']
    list_filter = ['is_readed']
    search_fields = ['email']
    list_editable = ['is_readed']

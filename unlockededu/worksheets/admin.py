from django.contrib import admin

from django.contrib.admin import AdminSite

# Register your models here.

from .models import Tag, Subject, FreeResponseQuestion, MultipleChoiceQuestion, MCAnswer


admin.site.site_header = 'UnlockedEdu'
admin.site.site_title = 'UnlockedEdu Admin'


class MCAnswerInline(admin.StackedInline):
    model = MCAnswer


class MCQuestionInline(admin.ModelAdmin):
    inlines = [MCAnswerInline]


admin.site.register(Tag)
admin.site.register(Subject)
admin.site.register(FreeResponseQuestion)
admin.site.register(MultipleChoiceQuestion, MCQuestionInline)


class UserAdminSite(AdminSite):
    site_header = 'UnlockedEdu Users'


user_admin = UserAdminSite(name='useradmin')
user_admin.register(FreeResponseQuestion)
user_admin.register(Tag)
user_admin.register(Subject)
user_admin.register(MultipleChoiceQuestion, MCQuestionInline)

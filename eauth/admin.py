from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from eauth.models import Profile

admin.site.site_header = 'eCourt - Administration'
admin.site.site_title = 'Tamil Nadu District Judiciary'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    #return super().formfield_for_foreignkey(db_field, request, **kwargs)

class CustomUserAdmin(UserAdmin):
    
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
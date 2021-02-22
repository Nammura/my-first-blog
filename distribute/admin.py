from django.contrib import admin
from .models import (Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Daytoday)


class DistAdmin(admin.ModelAdmin):
    list_display = (
    'member_name',
    'science_or_humanities',
    'only_for_science_menber_impossible_subject',
    'only_for_science_menber_no_good_subject'
    )
    
    list_display_links = None
    
    list_editable = (
    'science_or_humanities',
    'only_for_science_menber_impossible_subject',
    'only_for_science_menber_no_good_subject'
    )

    

admin.site.register(Sunday,DistAdmin)
admin.site.register(Monday,DistAdmin)
admin.site.register(Tuesday,DistAdmin)
admin.site.register(Wednesday,DistAdmin)
admin.site.register(Thursday,DistAdmin)
admin.site.register(Friday,DistAdmin)
admin.site.register(Saturday,DistAdmin)
admin.site.register(Daytoday)



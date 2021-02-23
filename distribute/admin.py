from django.contrib import admin
from .models import (Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Daytoday)
from django_pandas.io import read_frame
import pandas as pd


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
    
    def save_model(self, request, obj, form, change):
        super(DistAdmin, self).save_model(request, obj, form, change)
        
        sun = Sunday.objects.all()
        df_sun = read_frame(sun,fieldnames=['member_name'])
        sunday = []
        for i in df_sun.index:
            sunday.append('日')
        df_sun['曜日'] = sunday
        sun1 = []
        sun2 = []
        sun3 = []
        for i in df_sun.index:
            sun1.append(sun[i].science_or_humanities)
            sun2.append(sun[i].only_for_science_menber_impossible_subject)
            sun3.append(sun[i].only_for_science_menber_no_good_subject)
        df_sun['文理'] = sun1
        df_sun['対応不可能な科目'] = sun2
        df_sun['対応を控えたい科目'] = sun3
            
        
        mon = Monday.objects.all()
        df_mon = read_frame(mon,fieldnames=['member_name'])
        monday = []
        for i in df_mon.index:
            monday.append('月')
        df_mon['曜日'] = monday
        mon1 = []
        mon2 = []
        mon3 = []
        for i in df_mon.index:
            mon1.append(mon[i].science_or_humanities)
            mon2.append(mon[i].only_for_science_menber_impossible_subject)
            mon3.append(mon[i].only_for_science_menber_no_good_subject)
        df_mon['文理'] = mon1
        df_mon['対応不可能な科目'] = mon2
        df_mon['対応を控えたい科目'] = mon3
        
        tues = Tuesday.objects.all()
        df_tues = read_frame(tues,fieldnames=['member_name'])
        tuesday = []
        for i in df_tues.index:
            tuesday.append('火')
        df_tues['曜日'] = tuesday
        tues1 = []
        tues2 = []
        tues3 = []
        for i in df_tues.index:
            tues1.append(tues[i].science_or_humanities)
            tues2.append(tues[i].only_for_science_menber_impossible_subject)
            tues3.append(tues[i].only_for_science_menber_no_good_subject)
        df_tues['文理'] = tues1
        df_tues['対応不可能な科目'] = tues2
        df_tues['対応を控えたい科目'] = tues3
        
        
        wednes = Wednesday.objects.all()
        df_wednes = read_frame(wednes,fieldnames=['member_name'])
        wednesday = []
        for i in df_wednes.index:
            wednesday.append('水')
        df_wednes['曜日'] = wednesday
        wednes1 = []
        wednes2 = []
        wednes3 = []
        for i in df_wednes.index:
            wednes1.append(wednes[i].science_or_humanities)
            wednes2.append(wednes[i].only_for_science_menber_impossible_subject)
            wednes3.append(wednes[i].only_for_science_menber_no_good_subject)
        df_wednes['文理'] = wednes1
        df_wednes['対応不可能な科目'] = wednes2
        df_wednes['対応を控えたい科目'] = wednes3
        
        
        thurs = Thursday.objects.all()
        df_thurs = read_frame(thurs,fieldnames=['member_name'])
        thursday = []
        for i in df_thurs.index:
            thursday.append('木')
        df_thurs['曜日'] = thursday
        thurs1 = []
        thurs2 = []
        thurs3 = []
        for i in df_thurs.index:
            thurs1.append(thurs[i].science_or_humanities)
            thurs2.append(thurs[i].only_for_science_menber_impossible_subject)
            thurs3.append(thurs[i].only_for_science_menber_no_good_subject)
        df_thurs['文理'] = thurs1
        df_thurs['対応不可能な科目'] = thurs2
        df_thurs['対応を控えたい科目'] = thurs3
        
        
        fri = Friday.objects.all()
        df_fri = read_frame(fri,fieldnames=['member_name'])
        friday = []
        for i in df_fri.index:
            friday.append('金')
        df_fri['曜日'] = friday
        fri1 = []
        fri2 = []
        fri3 = []
        for i in df_fri.index:
            fri1.append(fri[i].science_or_humanities)
            fri2.append(fri[i].only_for_science_menber_impossible_subject)
            fri3.append(fri[i].only_for_science_menber_no_good_subject)
        df_fri['文理'] = fri1
        df_fri['対応不可能な科目'] = fri2
        df_fri['対応を控えたい科目'] = fri3
        
    
        
        satur = Saturday.objects.all()
        df_satur = read_frame(satur,fieldnames=['member_name',])
        saturday = []
        for i in df_satur.index:
            saturday.append('土')
        df_satur['曜日'] = saturday
        satur1 = []
        satur2 = []
        satur3 = []
        for i in df_satur.index:
            satur1.append(satur[i].science_or_humanities)
            satur2.append(satur[i].only_for_science_menber_impossible_subject)
            satur3.append(satur[i].only_for_science_menber_no_good_subject)
        df_satur['文理'] = satur1
        df_satur['対応不可能な科目'] = satur2
        df_satur['対応を控えたい科目'] = satur3
        
        df = pd.concat([df_sun,df_mon,df_tues,df_wednes,df_thurs,df_fri,df_satur])
        df.reset_index(drop=True,inplace=True)
        
        df.to_csv('/Users/nakamurayuuta/djangogirls/distribute/static/csv/リスト.csv')
    

admin.site.register(Sunday,DistAdmin)
admin.site.register(Monday,DistAdmin)
admin.site.register(Tuesday,DistAdmin)
admin.site.register(Wednesday,DistAdmin)
admin.site.register(Thursday,DistAdmin)
admin.site.register(Friday,DistAdmin)
admin.site.register(Saturday,DistAdmin)
admin.site.register(Daytoday)



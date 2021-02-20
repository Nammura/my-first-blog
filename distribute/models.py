from django.db import models
from multiselectfield import MultiSelectField


choice1 = (
    (1,'文系'),
    (2,'文系プラス'),
    (3,'理系'),
)

choice2 = (
    (1,'中学数学'),
    (2,'物理'),
    (3,'化学'),
    (4,'中学理科'),

)

choice3 = (
        (1,'日曜チーム'),
        (2,'月曜チーム'),
        (3,'火曜チーム'),
        (4,'水曜チーム'),
        (5,'木曜チーム'),
        (6,'金曜チーム'),
        (7,'土曜チーム'),
)

dayDict = {
    '1':'日曜チーム',
    '2':'月曜チーム',
    '3':'火曜チーム',
    '4':'水曜チーム',
    '5':'木曜チーム',
    '6':'金曜チーム',
    '7':'土曜チーム',
}



class Sunday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '日曜チーム'
        verbose_name_plural = '(a) 日曜チーム'
        
class Monday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '月曜チーム'
        verbose_name_plural = '(b) 月曜チーム'
        
class Tuesday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '火曜チーム'
        verbose_name_plural = '(c) 火曜チーム'
        
class Wednesday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '水曜チーム'
        verbose_name_plural = '(d) 水曜チーム'
        
class Thursday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '木曜チーム'
        verbose_name_plural = '(e) 木曜チーム'
        
class Friday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '金曜チーム'
        verbose_name_plural = '(f) 金曜チーム'
        
class Saturday(models.Model):
    member_name = models.CharField('名前',max_length=15)
    science_or_humanities = MultiSelectField('文理',choices = choice1)
    only_for_science_menber_impossible_subject = MultiSelectField('対応不可能な科目',choices = choice2,blank = True)
    only_for_science_menber_no_good_subject = MultiSelectField('対応を控えたい科目',choices = choice2, blank = True)
    
    def __str__(self):
        return self.member_name
        
    class Meta:
        verbose_name = '土曜チーム'
        verbose_name_plural = '(g) 土曜チーム'

class Daytoday(models.Model):
    days = MultiSelectField('曜日を選択',choices = choice3,blank=True)
    
    def __str__(self):
        if len(self.days) != 0:
            return dayDict[self.days[0]]
        else:
            return '未選択'
        
    class Meta:
        verbose_name = '現在のチーム'
        verbose_name_plural = '【チーム選択】'
        

    



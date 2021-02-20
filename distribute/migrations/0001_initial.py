# Generated by Django 2.2.18 on 2021-02-20 14:19

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Daytoday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '日曜チーム'), (2, '月曜チーム'), (3, '火曜チーム'), (4, '水曜チーム'), (5, '木曜チーム'), (6, '金曜チーム'), (7, '土曜チーム')], max_length=13, verbose_name='曜日を選択')),
            ],
            options={
                'verbose_name': '現在のチーム',
                'verbose_name_plural': '【チーム選択】',
            },
        ),
        migrations.CreateModel(
            name='Friday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '金曜チーム',
                'verbose_name_plural': '(f) 金曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Monday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '月曜チーム',
                'verbose_name_plural': '(b) 月曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Saturday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '土曜チーム',
                'verbose_name_plural': '(g) 土曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Sunday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '日曜チーム',
                'verbose_name_plural': '(a) 日曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Thursday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '木曜チーム',
                'verbose_name_plural': '(e) 木曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Tuesday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '火曜チーム',
                'verbose_name_plural': '(c) 火曜チーム',
            },
        ),
        migrations.CreateModel(
            name='Wednesday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=15, verbose_name='名前')),
                ('science_or_humanities', multiselectfield.db.fields.MultiSelectField(choices=[(1, '文系'), (2, '文系プラス'), (3, '理系')], max_length=5, verbose_name='文理')),
                ('only_for_science_menber_impossible_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応不可能な科目')),
                ('only_for_science_menber_no_good_subject', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(1, '中学数学'), (2, '物理'), (3, '化学'), (4, '中学理科')], max_length=7, verbose_name='対応を控えたい科目')),
            ],
            options={
                'verbose_name': '水曜チーム',
                'verbose_name_plural': '(d) 水曜チーム',
            },
        ),
    ]

# Generated by Django 2.0.5 on 2019-03-22 07:49

import activityRecord.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='actInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='活动名称')),
                ('phone', models.CharField(blank=True, max_length=11, verbose_name='负责人电话')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name': '活动列表',
                'verbose_name_plural': '活动列表',
            },
        ),
        migrations.CreateModel(
            name='actRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='活动时间')),
                ('address', models.CharField(default='无', max_length=128, verbose_name='活动地点')),
                ('score', models.IntegerField(default=2, verbose_name='活动得分')),
                ('duration', models.IntegerField(default=2, verbose_name='持续时间')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activityRecord.actInfo', verbose_name='活动名称')),
            ],
            options={
                'verbose_name': '活动记录',
                'verbose_name_plural': '活动记录',
            },
        ),
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女'), ('unknown', '未知')], default='male', max_length=8, verbose_name=' 性别')),
                ('phoneNum', models.CharField(blank=True, max_length=25, unique=True, verbose_name='电话')),
                ('mem_id', activityRecord.fields.IdField(blank=True, max_length=6, null=True, unique=True, verbose_name='编号')),
                ('notice', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('join_date', models.DateField(verbose_name='登记日期')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '党员信息',
                'verbose_name_plural': '党员信息',
            },
        ),
        migrations.AddField(
            model_name='actrecord',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activityRecord.MemberInfo', verbose_name='参加人员'),
        ),
    ]

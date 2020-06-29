# Generated by Django 3.0.7 on 2020-06-29 12:51

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200628_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='banner_subtitle',
            field=wagtail.core.fields.RichTextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='banner_title',
            field=models.CharField(blank=True, default='', max_length=100),
            preserve_default=False,
        ),
    ]

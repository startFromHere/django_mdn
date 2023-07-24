# Generated by Django 4.2.1 on 2023-07-24 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_date'], 'permissions': (('can_delete_comment', 'delete comment'),)},
        ),
        migrations.AlterModelOptions(
            name='blogger',
            options={'permissions': (('can_edit_blog', 'edit blog'),)},
        ),
    ]
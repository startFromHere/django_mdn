# Generated by Django 4.2.1 on 2023-07-24 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogger_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-create_date'], 'permissions': (('can_edit_blog', 'Can edit blog'), ('can_edit_blog1', 'Can edit blog1'))},
        ),
        migrations.AlterModelOptions(
            name='blogger',
            options={},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['post_date'], 'permissions': (('can_delete_comment', 'Can delete comment'),)},
        ),
    ]
# Generated by Django 4.2.1 on 2023-07-21 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of this blog', max_length=200)),
                ('content', models.TextField(help_text='blog content')),
                ('create_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-create_date'],
                'permissions': (('can_add_comment', 'add a comment'),),
            },
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('intro', models.TextField(help_text='info of this author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('content', models.TextField(help_text='comment content')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog')),
            ],
            options={
                'ordering': ['post_date'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogger'),
        ),
    ]

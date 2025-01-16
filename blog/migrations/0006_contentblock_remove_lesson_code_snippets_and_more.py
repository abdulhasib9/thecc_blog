# Generated by Django 5.1.4 on 2025-01-15 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_menu_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('code', 'Code Snippet')], max_length=10)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='content_images/')),
                ('code_language', models.CharField(blank=True, max_length=50, null=True)),
                ('order', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='code_snippets',
        ),
        migrations.RemoveField(
            model_name='post',
            name='code_snippets',
        ),
        migrations.RemoveField(
            model_name='image',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='images',
        ),
        migrations.RemoveField(
            model_name='post',
            name='other_images',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='post',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='content',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='urls',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='post',
            name='urls',
        ),
        migrations.AddField(
            model_name='menu',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='link',
            field=models.URLField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_items', to='blog.menuitem'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='secondary_image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='blog.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='content_blocks',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='blog.contentblock'),
        ),
        migrations.AddField(
            model_name='post',
            name='content_blocks',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blog.contentblock'),
        ),
        migrations.DeleteModel(
            name='CodeSnippet',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]

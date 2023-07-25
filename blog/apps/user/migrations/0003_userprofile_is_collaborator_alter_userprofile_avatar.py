# Generated by Django 4.2.3 on 2023-07-24 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofile_created_remove_userprofile_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_collaborator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='user/default/default.jpg', upload_to='user/avatars/'),
        ),
    ]

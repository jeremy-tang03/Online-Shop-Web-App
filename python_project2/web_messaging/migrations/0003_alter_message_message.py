# Generated by Django 4.0.4 on 2022-05-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_messaging', '0002_rename_msg_body_message_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=1500),
        ),
    ]

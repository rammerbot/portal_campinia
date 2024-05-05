# Generated by Django 5.0.4 on 2024-05-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_news_email_alter_contact_message_attachment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'verbose_name': 'Nueva Jornada', 'verbose_name_plural': 'Nuevas Jornadas'},
        ),
        migrations.AddField(
            model_name='attachment',
            name='date',
            field=models.DateField(null=True, verbose_name='Fecha de Jornada'),
        ),
    ]

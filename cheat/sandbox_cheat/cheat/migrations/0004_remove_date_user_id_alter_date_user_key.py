# Generated by Django 4.1.7 on 2023-03-18 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheat', '0003_history_date_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date_user',
            name='id',
        ),
        migrations.AlterField(
            model_name='date_user',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cheat.key_base'),
        ),
    ]
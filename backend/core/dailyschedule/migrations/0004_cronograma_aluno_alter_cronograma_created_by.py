# Generated by Django 4.1.4 on 2022-12-25 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dailyschedule', '0003_remove_cronograma_aluno_alter_cronograma_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronograma',
            name='aluno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dailyschedule.aluno'),
        ),
        migrations.AlterField(
            model_name='cronograma',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='criado por'),
        ),
    ]

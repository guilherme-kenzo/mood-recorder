# Generated by Django 4.1.3 on 2022-11-10 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BEM', 'Bem'), ('NEU', 'Neutro'), ('MAL', 'Mal')], max_length=255)),
                ('feeling', models.CharField(choices=[('OT', 'Otimismo'), ('CF', 'Confiante'), ('FL', 'Felicidade'), ('GR', 'Gratitude'), ('ID', 'Indiferenca'), ('CE', 'Cetico'), ('DE', 'Depressao'), ('AN', 'Ansiedade'), ('DN', 'Desanimo')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mood')),
            ],
        ),
    ]

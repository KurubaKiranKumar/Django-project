# Generated by Django 2.2.2 on 2019-06-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminzone', '0003_packet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicantquali', models.CharField(max_length=10)),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-13 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firewall_rules', '0003_firewall_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='firewall_rules',
            name='firewall_practice_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firewall_rules.firewall_practice'),
        ),
        migrations.AddField(
            model_name='interface',
            name='firewall_practice_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firewall_rules.firewall_practice'),
        ),
        migrations.AddField(
            model_name='nat_rules',
            name='firewall_practice_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firewall_rules.firewall_practice'),
        ),
        migrations.AddField(
            model_name='route_table',
            name='firewall_practice_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='firewall_rules.firewall_practice'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

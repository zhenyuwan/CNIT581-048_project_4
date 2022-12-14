# Generated by Django 4.1.2 on 2022-10-24 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='firewall_rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=40)),
                ('direction', models.CharField(max_length=3)),
                ('source_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('source_protocol', models.CharField(max_length=3)),
                ('source_detail', models.CharField(max_length=5)),
                ('destination_ip', models.GenericIPAddressField(protocol='IPv4')),
                ('destination_protocol', models.CharField(max_length=3)),
                ('destination_detail', models.CharField(max_length=5)),
                ('action', models.CharField(max_length=5)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=40)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('subnet_mask', models.GenericIPAddressField(protocol='IPv4')),
            ],
        ),
        migrations.CreateModel(
            name='nat_rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nat_type', models.CharField(max_length=4)),
                ('host_name', models.CharField(max_length=40)),
                ('actual_zone', models.CharField(max_length=40)),
                ('actual_address', models.GenericIPAddressField(protocol='IPv4')),
                ('actual_subnet_mask', models.GenericIPAddressField(protocol='IPv4')),
                ('mapped_zone', models.CharField(max_length=40)),
                ('mapped_address', models.GenericIPAddressField(protocol='IPv4')),
                ('mapped_subnet_mask', models.GenericIPAddressField(protocol='IPv4')),
            ],
        ),
        migrations.CreateModel(
            name='route_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=18)),
                ('next_hop', models.GenericIPAddressField(protocol='IPv4')),
                ('interface', models.CharField(max_length=20)),
                ('metric', models.PositiveSmallIntegerField()),
            ],
        ),
    ]

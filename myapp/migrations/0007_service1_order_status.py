# Generated by Django 5.0.3 on 2024-05-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_service1_service2'),
    ]

    operations = [
        migrations.AddField(
            model_name='service1',
            name='order_status',
            field=models.CharField(blank=True, choices=[('Processing', 'processing'), ('On-Hold', 'On-Hold'), ('Cancel', 'Cancel'), ('Picked Up', 'Picked up'), ('Completed', 'Completed')], max_length=50, null=True),
        ),
    ]
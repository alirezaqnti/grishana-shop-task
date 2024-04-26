# Generated by Django 3.0.14 on 2024-04-26 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='myshop.Product')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'ProductTable',
                'verbose_name_plural': 'ProductTables',
            },
            bases=('myshop.product',),
        ),
    ]

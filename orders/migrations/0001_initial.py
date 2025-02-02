# Generated by Django 4.0.2 on 2023-03-14 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0009_alter_comment_body_alter_product_description'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Family')),
                ('phone_number', models.CharField(max_length=15, verbose_name='PhoneNumber')),
                ('address', models.CharField(max_length=700, verbose_name='Address')),
                ('order_note', models.CharField(blank=True, max_length=700, verbose_name='توجه')),
                ('datetime_create', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Modified Time')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is_Paid?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.product')),
            ],
        ),
    ]

# Generated by Django 3.0.6 on 2020-06-27 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=200)),
                ('balcony', models.BooleanField(default=False)),
                ('cost_per_night', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Bedtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('extra_bed', models.BooleanField(default=False)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Guestnum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('booking', models.ManyToManyField(blank=True, related_name='guests', to='hotel.Booking')),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='bed_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Bedtype'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='max_number_of_guests',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Guestnum'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='room_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.Category'),
        ),
    ]
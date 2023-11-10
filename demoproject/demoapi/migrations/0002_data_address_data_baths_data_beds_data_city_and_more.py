# Generated by Django 4.2.7 on 2023-11-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demoapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="address",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="baths",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="data",
            name="beds",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="days_on_market",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="favorite",
            field=models.CharField(
                choices=[("Y", "Y"), ("N", "N")], default="N", max_length=1
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="data",
            name="hoa_per_month",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="interested",
            field=models.CharField(
                choices=[("Y", "Y"), ("N", "N")], default="Y", max_length=1
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="data",
            name="latitude",
            field=models.DecimalField(
                blank=True, decimal_places=5, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="data",
            name="location",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="longtitude",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="data",
            name="lot_size",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="mls_n0",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="next_open_house_end_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="next_open_house_start_time",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="data",
            name="price_per_square_feet",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="property_type",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="source",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="square_feet",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="state_or_province",
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="status",
            field=models.CharField(
                blank=True, choices=[("Active", "Active")], max_length=20, null=True
            ),
        ),
        migrations.AddField(
            model_name="data",
            name="url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="year_built",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="data",
            name="zip_or_postal_code",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="data",
            name="sold_date",
            field=models.DateField(auto_now=True),
        ),
    ]
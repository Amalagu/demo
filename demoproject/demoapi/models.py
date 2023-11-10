from django.db import models

# Create your models here.
class Data(models.Model):
    status_list = [('Active', 'Active')]
    yes_or_no_list = [('Y', 'Y'),('N', 'N')]
    sale_type = models.CharField(max_length=200, blank=True, null=True)
    sold_date = models.DateField(blank=True, null=True)
    property_type = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_or_province = models.CharField(max_length=2, blank=True, null=True)
    zip_or_postal_code = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    beds = models.IntegerField(blank=True, null=True)
    baths = models.DecimalField(max_digits=5,decimal_places=1, blank=True, null=True )
    location = models.CharField(max_length=200, blank=True, null=True)
    square_feet = models.IntegerField(blank=True, null=True)
    lot_size = models.IntegerField(blank=True, null=True)
    year_built = models.IntegerField(blank=True, null=True)
    days_on_market = models.IntegerField(blank=True, null=True)
    price_per_square_feet = models.IntegerField(blank=True, null=True)
    hoa_per_month = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=status_list, max_length=20, blank=True, null=True)
    next_open_house_start_time = models.CharField(max_length=50, blank=True, null=True)
    next_open_house_end_time = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    mls_n0 = models.IntegerField(blank=True, null=True)
    favorite = models.CharField(choices=yes_or_no_list, max_length=1)
    interested = models.CharField(choices=yes_or_no_list, max_length=1)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10,decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.sale_type
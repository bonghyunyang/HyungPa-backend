import csv
import os
import django
import sys

os.chdir(".")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brother.settings")
django.setup()

from product.models import *

CSV_PATH = 'product.csv'

with open(CSV_PATH, newline = '') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        Product.objects.create(
            name             = row['product'],
            price            = row['price'],
            capacity         = row['capacity'],
            product_image    = row['product_image'],
            like_nums        = row['like_number'],
            review_nums      = row['review'],
            mini_nums        = row['mini'],
            brand_name       = row['brand'],
            firstcategory    = FirstCategory.objects.get(id = row['first_category']),
            secondcategory   = SecondCategory.objects.get(id = row['second_category'])
        )

from datetime import date, time, timedelta

from django.db import models
from django.utils import timezone

import django_cached_field as dcf


class TestItAll(models.Model):
    big_integer_field = dcf.CachedBigIntegerField()
    boolean_field = dcf.CachedBooleanField()
    char_field = dcf.CachedCharField(max_length=20)
    date_field = dcf.CachedDateField()
    datetime_field = dcf.CachedDateTimeField()
    decimal_field = dcf.CachedDecimalField(max_digits=2, decimal_places=1)
    email_field = dcf.CachedEmailField()
    float_field = dcf.CachedFloatField()
    integer_field = dcf.CachedIntegerField()
    null_boolean_field = dcf.CachedNullBooleanField()
    positive_integer_field = dcf.CachedPositiveIntegerField()
    positive_small_integer_field = dcf.CachedPositiveSmallIntegerField()
    slug_field = dcf.CachedSlugField()
    small_integer_field = dcf.CachedSmallIntegerField()
    text_field = dcf.CachedTextField()
    time_field = dcf.CachedTimeField()

    def calculate_big_integer_field(self):
        return 181010470182094194

    def calculate_boolean_field(self):
        return False

    def calculate_char_field(self):
        return "method"

    def calculate_date_field(self):
        return date.today()

    def calculate_datetime_field(self):
        return timezone.now() + timedelta(days=1)

    def calculate_decimal_field(self):
        return "0.9"

    def calculate_email_field(self):
        return "model@example.com"

    def calculate_float_field(self):
        return 3.14159

    def calculate_integer_field(self):
        return -184017

    def calculate_null_boolean_field(self):
        return False

    def calculate_positive_integer_field(self):
        return 19471974

    def calculate_positive_small_integer_field(self):
        return 3

    def calculate_slug_field(self):
        return "slughornwashere"

    def calculate_small_integer_field(self):
        return -2

    def calculate_text_field(self):
        return "fields of text"

    def calculate_time_field(self):
        return time.max

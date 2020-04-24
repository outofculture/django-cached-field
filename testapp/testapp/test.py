from datetime import date, time, timedelta

from django.test import TestCase
from django.utils import timezone

from .models import TestItAll


class TestDjangoCachedField(TestCase):
    def test_all_the_field_are_fine(self):
        test = TestItAll()
        self.assertIsNotNone(test)

        test.recalculate_big_integer_field()
        test.recalculate_boolean_field()
        test.recalculate_char_field()
        test.recalculate_date_field()
        test.recalculate_datetime_field()
        test.recalculate_decimal_field()
        test.recalculate_email_field()
        test.recalculate_float_field()
        test.recalculate_integer_field()
        test.recalculate_null_boolean_field()
        test.recalculate_positive_integer_field()
        test.recalculate_positive_small_integer_field()
        test.recalculate_slug_field()
        test.recalculate_small_integer_field()
        test.recalculate_text_field()
        test.recalculate_time_field()

        self.assertIsNotNone(test.big_integer_field)
        self.assertIsNotNone(test.boolean_field)
        self.assertIsNotNone(test.char_field)
        self.assertIsNotNone(test.date_field)
        self.assertIsNotNone(test.datetime_field)
        self.assertIsNotNone(test.decimal_field)
        self.assertIsNotNone(test.email_field)
        self.assertIsNotNone(test.float_field)
        self.assertIsNotNone(test.integer_field)
        self.assertIsNotNone(test.null_boolean_field)
        self.assertIsNotNone(test.positive_integer_field)
        self.assertIsNotNone(test.positive_small_integer_field)
        self.assertIsNotNone(test.slug_field)
        self.assertIsNotNone(test.small_integer_field)
        self.assertIsNotNone(test.text_field)
        self.assertIsNotNone(test.time_field)

        test.big_integer_field = 1810381830183
        test.boolean_field = True
        test.char_field = "char"
        test.date_field = date.min
        test.datetime_field = timezone.now()
        test.decimal_field = "1.1"
        test.email_field = "test@example.com"
        test.float_field = 2.9999
        test.integer_field = -100000
        test.null_boolean_field = True
        test.positive_integer_field = 1000
        test.positive_small_integer_field = 2
        test.slug_field = "iamaslug"
        test.small_integer_field = -1
        test.text_field = "texty"
        test.time_field = time.min

        self.assertNotEqual(test.calculate_big_integer_field(), test.big_integer_field)
        self.assertNotEqual(test.calculate_boolean_field(), test.boolean_field)
        self.assertNotEqual(test.calculate_char_field(), test.char_field)
        self.assertNotEqual(test.calculate_date_field(), test.date_field)
        self.assertNotAlmostEqual(test.calculate_datetime_field(), test.datetime_field, delta=timedelta(seconds=1))
        self.assertNotEqual(test.calculate_decimal_field(), test.decimal_field)
        self.assertNotEqual(test.calculate_email_field(), test.email_field)
        self.assertNotEqual(test.calculate_float_field(), test.float_field)
        self.assertNotEqual(test.calculate_integer_field(), test.integer_field)
        self.assertNotEqual(test.calculate_null_boolean_field(), test.null_boolean_field)
        self.assertNotEqual(test.calculate_positive_integer_field(), test.positive_integer_field)
        self.assertNotEqual(test.calculate_positive_small_integer_field(), test.positive_small_integer_field)
        self.assertNotEqual(test.calculate_slug_field(), test.slug_field)
        self.assertNotEqual(test.calculate_small_integer_field(), test.small_integer_field)
        self.assertNotEqual(test.calculate_text_field(), test.text_field)
        self.assertNotEqual(test.calculate_time_field(), test.time_field)

        test.save()
        test = TestItAll.objects.get(id=test.id)

        test.flag_big_integer_field_as_stale()
        test.flag_boolean_field_as_stale()
        test.flag_char_field_as_stale()
        test.flag_date_field_as_stale()
        test.flag_datetime_field_as_stale()
        test.flag_decimal_field_as_stale()
        test.flag_email_field_as_stale()
        test.flag_float_field_as_stale()
        test.flag_integer_field_as_stale()
        test.flag_null_boolean_field_as_stale()
        test.flag_positive_integer_field_as_stale()
        test.flag_positive_small_integer_field_as_stale()
        test.flag_slug_field_as_stale()
        test.flag_small_integer_field_as_stale()
        test.flag_text_field_as_stale()
        test.flag_time_field_as_stale()

        self.assertEqual(test.calculate_big_integer_field(), test.big_integer_field)
        self.assertEqual(test.calculate_boolean_field(), test.boolean_field)
        self.assertEqual(test.calculate_char_field(), test.char_field)
        self.assertEqual(test.calculate_date_field(), test.date_field)
        self.assertAlmostEqual(test.calculate_datetime_field(), test.datetime_field, delta=timedelta(seconds=1))
        self.assertEqual(test.calculate_decimal_field(), test.decimal_field)
        self.assertEqual(test.calculate_email_field(), test.email_field)
        self.assertEqual(test.calculate_float_field(), test.float_field)
        self.assertEqual(test.calculate_integer_field(), test.integer_field)
        self.assertEqual(test.calculate_null_boolean_field(), test.null_boolean_field)
        self.assertEqual(test.calculate_positive_integer_field(), test.positive_integer_field)
        self.assertEqual(test.calculate_positive_small_integer_field(), test.positive_small_integer_field)
        self.assertEqual(test.calculate_slug_field(), test.slug_field)
        self.assertEqual(test.calculate_small_integer_field(), test.small_integer_field)
        self.assertEqual(test.calculate_text_field(), test.text_field)
        self.assertEqual(test.calculate_time_field(), test.time_field)

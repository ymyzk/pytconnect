#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import date
import unittest

from pytconnect.report import (Period, ProductTypeIdentifier, PromotionalCode,
                               ReportRecord, Subscription)


class ReportRecordTests(unittest.TestCase):
    def test_from_dict(self):
        d = {
            'Provider': 'APPLE',
            'Provider Country': 'US',
            'SKU': 'SKU123',
            'Developer': 'Developer, Inc.',
            'Title': 'My App',
            'Version': '1.2.3',
            'Product Type Identifier': '1F',
            'Units': '32',
            'Developer Proceeds': '9.5',
            'Begin Date': '10/11/2014',
            'End Date': '10/11/2014',
            'Customer Currency': 'JPY',
            'Country Code': 'JP',
            'Currency of Proceeds': 'JPY',
            'Apple Identifier': '123456789',
            'Customer Price': '10.5',
            'Promo Code': 'GP',
            'Parent Identifier': '',
            'Subscription': 'New',
            'Period': '7 Days',
            'Category': 'Games',
            'CMB': ''
        }
        r = ReportRecord.from_dict(d)
        self.assertEqual(d['Provider'], r.provider)
        self.assertEqual(d['Provider Country'], r.provider_country)
        self.assertEqual(d['SKU'], r.sku)
        self.assertEqual(d['Developer'], r.developer)
        self.assertEqual(d['Title'], r.title)
        self.assertEqual((1, 2, 3), r.version)
        self.assertIs(ProductTypeIdentifier.universal_install,
                      r.product_type_identifier)
        self.assertEqual(int(d['Units']), r.units)
        self.assertEqual(float(d['Developer Proceeds']), r.developer_proceeds)
        self.assertEqual(date(2014, 10, 11), r.begin_date)
        self.assertEqual(date(2014, 10, 11), r.end_date)
        self.assertEqual(d['Customer Currency'], r.customer_currency)
        self.assertEqual(d['Country Code'], r.country_code)
        self.assertEqual(d['Currency of Proceeds'], r.currency_of_proceeds)
        self.assertEqual(int(d['Apple Identifier']), r.apple_identifier)
        self.assertEqual(float(d['Customer Price']), r.customer_price)
        self.assertIs(PromotionalCode.gift_purchase, r.promo_code)
        self.assertEqual(d['Parent Identifier'], r.parent_identifier)
        self.assertIs(Subscription.new, r.subscription)
        self.assertIs(Period.period_7_days, r.period)
        self.assertEqual(d['Category'], r.category)
        self.assertEqual(d['CMB'], r.cmb)
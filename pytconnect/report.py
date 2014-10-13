#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from datetime import date
from enum import Enum
import operator


class ProductTypeIdentifier(Enum):
    iphone_install = '1'
    app_bundle = '1-B'
    iphone_update = '7'
    ios_in_app_purchase = 'IA1'
    ios_in_app_subscription = 'IA9'
    ios_in_app_auto_renewable_subscription = 'IAY'
    ios_in_app_free_subscription = 'IAC'
    universal_install = '1F'
    universal_update = '7F'
    ipad_install = '1T'
    ipad_update = '7T'
    mac_install = 'F1'
    mac_update = 'F7'
    mac_in_app_purchase = 'FI1'
    iphone_custom = '1E'
    ipad_custom = '1EP'
    universal_custom = '1EU'


class PromotionalCode(Enum):
    developer = 'CR - RW'
    gift_purchase = 'GP'
    gift_redemption = 'GR'  # Deprecated in Sep. 2013
    education = 'EDU'


class Subscription(Enum):
    new = 'New'
    renewal = 'Renewal'


class Period(Enum):
    period_7_days = '7 Days'
    period_1_month = '1 Month'
    period_2_months = '2 Months'
    period_3_months = '3 Months'
    period_6_months = '6 Months'
    period_1_year = '1 Year'


class ReportRecord(object):
    def __init__(self, **kwargs):
        self.provider = kwargs.get('provider', '')
        self.provider_country = kwargs.get('provider_country', '')
        self.sku = kwargs.get('sku', '')
        self.developer = kwargs.get('developer', '')
        self.title = kwargs.get('title', '')
        self.version = kwargs.get('version', tuple())
        self.product_type_identifier = kwargs.get('product_type_identifier',
                                                  '')
        self.units = kwargs.get('units', 0)
        self.developer_proceeds = kwargs.get('developer_proceeds', 0.0)
        self.begin_date = kwargs.get('begin_date', date.min)
        self.end_date = kwargs.get('end_date', date.min)
        self.customer_currency = kwargs.get('customer_currency', '')
        self.country_code = kwargs.get('country_code', '')
        self.currency_of_proceeds = kwargs.get('currency_of_proceeds', '')
        self.apple_identifier = kwargs.get('apple_identifier', 0)
        self.customer_price = kwargs.get('customer_price', 0.0)
        self.promo_code = kwargs.get('promo_code', '')
        self.parent_identifier = kwargs.get('parent_identifier', '')
        self.subscription = kwargs.get('subscription', '')
        self.period = kwargs.get('period', '')
        self.category = kwargs.get('category', '')
        self.cmb = kwargs.get('cmb', '')

    _dict_to_kwargs_str = {
        'Provider': 'provider',
        'Provider Country': 'provider_country',
        'SKU': 'sku',
        'Developer': 'developer',
        'Title': 'title',
        'Customer Currency': 'customer_currency',
        'Country Code': 'country_code',
        'Currency of Proceeds': 'currency_of_proceeds',
        'Parent Identifier': 'parent_identifier',
        'Category': 'category',
        'CMB': 'cmb'
    }

    _dict_to_kwargs_int = {
        'Units': 'units',
        'Apple Identifier': 'apple_identifier',
    }

    _dict_to_kwargs_float = {
        'Developer Proceeds': 'developer_proceeds',
        'Customer Price': 'customer_price'
    }

    _dict_to_kwargs_date = {
        'Begin Date': 'begin_date',
        'End Date': 'end_date'
    }

    _str_to_product_type_identifier = {
        '1': ProductTypeIdentifier.iphone_install,
        '1-B': ProductTypeIdentifier.app_bundle,
        '7': ProductTypeIdentifier.iphone_update,
        'IA1': ProductTypeIdentifier.ios_in_app_purchase,
        'IA9': ProductTypeIdentifier.ios_in_app_subscription,
        'IAY': ProductTypeIdentifier.ios_in_app_auto_renewable_subscription,
        'IAC': ProductTypeIdentifier.ios_in_app_free_subscription,
        '1F': ProductTypeIdentifier.universal_install,
        '7F': ProductTypeIdentifier.universal_update,
        '1T': ProductTypeIdentifier.ipad_install,
        '7T': ProductTypeIdentifier.ipad_update,
        'F1': ProductTypeIdentifier.mac_install,
        'F7': ProductTypeIdentifier.mac_update,
        'FI1': ProductTypeIdentifier.mac_in_app_purchase,
        '1E': ProductTypeIdentifier.iphone_custom,
        '1EP': ProductTypeIdentifier.ipad_custom,
        '1EU': ProductTypeIdentifier.universal_custom
    }

    _str_to_promotional_code = {
        'CR - RW': PromotionalCode.developer,
        'GP': PromotionalCode.gift_purchase,
        'GR': PromotionalCode.gift_redemption,
        'EDU': PromotionalCode.education
    }

    _str_to_subscription = {
        'New': Subscription.new,
        'Renewal': Subscription.renewal
    }

    _str_to_period = {
        '7 Days': Period.period_7_days,
        '1 Month': Period.period_1_month,
        '2 Months': Period.period_2_months,
        '3 Months': Period.period_3_months,
        '6 Months': Period.period_6_months,
        '1 Year': Period.period_1_year
    }

    @staticmethod
    def from_dict(d):
        """Create ReportRecord object from dictionary

        :param dict d: dictionary (str: str or unicode: unicode)
        """""
        kwargs = {}

        for key, kwarg in ReportRecord._dict_to_kwargs_str.items():
            if key in d:
                kwargs[kwarg] = d[key]

        for key, kwarg in ReportRecord._dict_to_kwargs_int.items():
            if key in d:
                kwargs[kwarg] = int(d[key])

        for key, kwarg in ReportRecord._dict_to_kwargs_float.items():
            if key in d:
                kwargs[kwarg] = float(d[key])

        for key, kwarg in ReportRecord._dict_to_kwargs_date.items():
            if key in d:
                # Format: MM-DD-YYYY
                mdy = tuple(map(int, d[key].split('/')))
                kwargs[kwarg] = date(mdy[2], mdy[0], mdy[1])

        if 'Version' in d:
            version = tuple(map(int, d['Version'].split('.')))
            kwargs['version'] = version

        if 'Product Type Identifier' in d:
            ptis = d['Product Type Identifier']
            if ptis in ReportRecord._str_to_product_type_identifier:
                pti = ReportRecord._str_to_product_type_identifier[ptis]
                kwargs['product_type_identifier'] = pti

        if 'Promo Code' in d:
            pcs = d['Promo Code']
            if pcs in ReportRecord._str_to_promotional_code:
                pc = ReportRecord._str_to_promotional_code[pcs]
                kwargs['promo_code'] = pc

        if 'Subscription' in d:
            ss = d['Subscription']
            if ss in ReportRecord._str_to_subscription:
                s = ReportRecord._str_to_subscription[ss]
                kwargs['subscription'] = s

        if 'Period' in d:
            ps = d['Period']
            if ps in ReportRecord._str_to_period:
                kwargs['period'] = ReportRecord._str_to_period[ps]

        return ReportRecord(**kwargs)


class Report(object):
    def __init__(self, records=None):
        if records is None:
            records = []

        self.records = records

    def append(self, record):
        self.records.append(record)

    _filter_kwargs = {
        'provider',
        'provider_country',
        'sku',
        'developer',
        'title',
        'version',
        'product_type_identifier',
        'units',
        'developer_proceeds',
        'begin_date',
        'end_date',
        'customer_currency',
        'country_code',
        'currency_of_proceeds',
        'apple_identifier',
        'customer_price',
        'promo_code',
        'parent_identifier',
        'subscription',
        'period',
        'category',
        'cmb'
    }

    _filter_operators = {
        'eq': operator.eq,
        'gt': operator.gt,
        'gte': operator.ge,
        'lt': operator.lt,
        'lte': operator.le
    }

    def filter(self, **kwargs):
        records = self.records

        for kwarg, value in kwargs.items():
            kw = kwarg.split('__')
            if kw[0] in self._filter_kwargs:
                op = self._filter_operators.get(kw[-1], operator.eq)
                records = filter(lambda r: op(getattr(r, kw[0]), value),
                                 records)

        if 'date' in kwargs:
            d = kwargs['date']
            records = filter(lambda r: r.begin_date <= d <= r.end_date,
                             records)

        if 'date__gt' in kwargs:
            records = filter(lambda r: kwargs['date__gt'] < r.end_date,
                             records)

        if 'date__gte' in kwargs:
            records = filter(lambda r: kwargs['date__gte'] <= r.end_date,
                             records)

        if 'date__lt' in kwargs:
            records = filter(lambda r: r.begin_date < kwargs['date__lt'],
                             records)

        if 'date__lte' in kwargs:
            records = filter(lambda r: r.begin_date <= kwargs['date__lte'],
                             records)

        return Report(list(records))

    def __add__(self, other):
        if isinstance(other, Report):
            return Report(self.records + other.records)
        raise NotImplemented

    # Properties

    @property
    def providers(self):
        return sorted(set(map(lambda r: r.provider, self.records)))

    @property
    def provider_countries(self):
        return sorted(set(map(lambda r: r.provider_country, self.records)))

    @property
    def developers(self):
        return sorted(set(map(lambda r: r.developer, self.records)))

    @property
    def titles(self):
        return sorted(set(map(lambda r: r.title, self.records)))

    @property
    def versions(self):
        return sorted(set(map(lambda r: r.version, self.records)))

    @property
    def skus(self):
        return sorted(set(map(lambda r: r.sku, self.records)))

    @property
    def product_type_identifiers(self):
        return list(set(map(lambda r: r.product_type_identifier,
                            self.records)))

    @property
    def units(self):
        return sum(map(lambda r: r.units, self.records))

    @property
    def developer_proceeds(self):
        return sorted(set(map(lambda r: r.developer_proceeds, self.records)))

    @property
    def customer_currencies(self):
        return sorted(set(map(lambda r: r.customer_currency, self.records)))

    @property
    def country_codes(self):
        return sorted(set(map(lambda r: r.country_codes, self.records)))

    @property
    def currencies_of_proceeds(self):
        return sorted(set(map(lambda r: r.currency_of_proceeds, self.records)))

    @property
    def apple_identifiers(self):
        return sorted(set(map(lambda r: r.apple_identifier, self.records)))

    @property
    def customer_prices(self):
        return sorted(set(map(lambda r: r.customer_price, self.records)))

    @property
    def promo_codes(self):
        return sorted(set(map(lambda r: r.promo_code, self.records)))

    @property
    def parent_identifiers(self):
        return sorted(set(map(lambda r: r.parent_identifier, self.records)))

    @property
    def subscriptions(self):
        return sorted(set(map(lambda r: r.subscription, self.records)))

    @property
    def periods(self):
        return sorted(set(map(lambda r: r.period, self.records)))

    @property
    def categories(self):
        return sorted(set(map(lambda r: r.category, self.records)))

    @property
    def cmbs(self):
        return sorted(set(map(lambda r: r.cmb, self.records)))
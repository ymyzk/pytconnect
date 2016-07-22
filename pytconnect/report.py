# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from enum import Enum
import os

import pandas as pd


class ProductTypeIdentifier(Enum):
    iphone_install = "1"
    iphone_update = "7"
    app_bundle = "1-B"
    iphone_custom = "1E"
    ipad_custom = "1EP"
    universal_custom = "1EU"
    universal_install = "1F"
    ipad_install = "1T"
    universal_update = "7F"
    ipad_update = "7T"
    mac_install = "F1"
    mac_update = "F7"
    mac_in_app_purchase = "FI1"
    ios_in_app_purchase_purchase = "IA1"
    mac_in_app_purchase_purchase = "IA1-M"
    ios_in_app_purchase_subscription = "IA9"
    mac_in_app_purchase_subscription = "IA9-M"
    ios_in_app_purchase_free_subscription = "IAC"
    mac_in_app_purchase_free_subscription = "IAC-M"
    ios_in_app_purchase_auto_renewable_subscription = "IAY"
    mac_in_app_purchase_auto_renewable_subscription = "IAY-M"


class PromotionalCode(Enum):
    developer = "CR - RW"
    gift_purchase = "GP"
    gift_redemption = "GR"  # Deprecated in Sep. 2013
    education = "EDU"


class Subscription(Enum):
    new = "New"
    renewal = "Renewal"


class Period(Enum):
    period_7_days = "7 Days"
    period_1_month = "1 Month"
    period_2_months = "2 Months"
    period_3_months = "3 Months"
    period_6_months = "6 Months"
    period_1_year = "1 Year"


def load_files(directory):
    paths = map(lambda f: os.path.join(directory, f), os.listdir(directory))
    reports = map(load_file, paths)
    return pd.concat(reports, ignore_index=True)


def load_file(name):
    # Constants
    header_names = (
       "provider", "provider_country", "sku", "developer", "title", "version",
       "product_type_identifier", "units", "developer_proceeds", "begin_date",
       "end_date", "customer_currency", "country_code", "currency_of_proceeds",
       "apple_identifier", "customer_price", "promo_code", "parent_identifier",
       "subscription", "period", "category", "cmb", "device",
       "supported_platforms", "proceeds_reason")
    series_names_casted_to_datetime = ("begin_date", "end_date")
    series_names_casted_to_str = (
        "provider", "provider_country", "sku", "developer", "title", "version",
        "product_type_identifier", "customer_currency", "country_code",
        "currency_of_proceeds", "promo_code", "parent_identifier",
        "subscription", "period", "category", "cmb", "device",
        "supported_platforms", "proceeds_reason")
    series_names_casted_to_int = ("units", "apple_identifier")
    series_names_casted_to_float = ("developer_proceeds", "customer_price")

    # Load
    df = pd.read_csv(name, delimiter="\t", names=header_names, skiprows=1)

    # Cast
    for name in series_names_casted_to_datetime:
        df[name] = pd.to_datetime(df[name], format="%m/%d/%Y")
    for name in series_names_casted_to_str:
        df[name] = df[name].astype(str)
    for name in series_names_casted_to_int:
        df[name] = df[name].astype(int)
    for name in series_names_casted_to_float:
        df[name] = df[name].astype(float)
    df.version = df.version.apply(lambda v: tuple(map(int, v.split(".")))
                                  if v != "" and v != "nan" else ())

    return df

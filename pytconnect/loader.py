#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from pytconnect.report import Report, ReportRecord


def load(fp):
    """Load daily sales report file

    :param file fp:
    """
    report = Report()
    header = fp.readline().strip().split('\t')
    for line in fp:
        values = line.strip().split('\t')
        report.append(ReportRecord.from_dict(dict(zip(header, values))))
    return report
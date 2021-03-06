#!/usr/bin/env python3
# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
#
# Copyright (c) 2020 Authors and contributors
#
# Released under the GNU Public Licence, v2 or any higher version
# SPDX-License-Identifier: GPL-2.0-or-later

import pytest
import sys

# Workaround since we have no real module
sys.path.append("..")

from cli_main import convert_str_time


@pytest.mark.parametrize('x, frame',
                         (('1', 1),
                          ('-1', -1),
                          ('1ns', 1000),
                          ('12e3', 12e3),
                          ('12e3ps', 12e3)))
def test_convert_str_time(x, frame):
    assert frame == convert_str_time(x, dt=1)


def test_convert_str_time_dt():
    assert 1 == convert_str_time("10ps", dt=10)


def test_convert_str_time_raise():
    with pytest.raises(ValueError):
        convert_str_time('0.1', dt=1)

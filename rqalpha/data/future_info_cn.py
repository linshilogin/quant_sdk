# -*- coding: utf-8 -*-
#
# Copyright 2019 Ricequant, Inc
#
# * Commercial Usage: please contact public@ricequant.com
# * Non-Commercial Usage:
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

from rqalpha.const import COMMISSION_TYPE

CN_FUTURE_INFO = {
    'A': {'close_commission_ratio': 2.0,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.0,
          'tick_size': 1.0},
    'AG': {'close_commission_ratio': 5e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 5e-05,
           'tick_size': 1.0},
    'AL': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 5.0},
    'AP': {'close_commission_ratio': 1.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 1.5,
           'tick_size': 1.0},
    'AU': {'close_commission_ratio': 10.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 10.0,
           'tick_size': 0.05},
    'B': {'close_commission_ratio': 2.0,
          'close_commission_today_ratio': 2.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.0,
          'tick_size': 1.0},
    'BB': {'close_commission_ratio': 0.0001,
           'close_commission_today_ratio': 5e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 0.0001,
           'tick_size': 0.05},
    'BU': {'close_commission_ratio': 3e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 3e-05,
           'tick_size': 2.0},
    'C': {'close_commission_ratio': 1.2,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 1.2,
          'tick_size': 1.0},
    'CF': {'close_commission_ratio': 4.3,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 4.3,
           'tick_size': 5.0},
    'CS': {'close_commission_ratio': 1.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 1.5,
           'tick_size': 1.0},
    'CU': {'close_commission_ratio': 2.5e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 2.5e-05,
           'tick_size': 10.0},
    'CY': {'close_commission_ratio': 4.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 4.0,
           'tick_size': 5.0},
    'ER': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 2.5,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 1.0},
    'FB': {'close_commission_ratio': 0.0001,
           'close_commission_today_ratio': 5e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 0.0001,
           'tick_size': 0.05},
    'FG': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 1.0},
    'FU': {'close_commission_ratio': 2e-05,
           'close_commission_today_ratio': 2e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 2e-05,
           'tick_size': 1.0},
    'HC': {'close_commission_ratio': 4e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 4e-05,
           'tick_size': 1.0},
    'I': {'close_commission_ratio': 6e-05,
          'close_commission_today_ratio': 3e-05,
          'commission_type': COMMISSION_TYPE.BY_MONEY,
          'open_commission_ratio': 6e-05,
          'tick_size': 0.5},
    'IC': {'close_commission_ratio': 2.3e-05,
           'close_commission_today_ratio': 0.0023,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 2.3e-05,
           'tick_size': 0.2},
    'IF': {'close_commission_ratio': 2.3e-05,
           'close_commission_today_ratio': 0.0023,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 2.3e-05,
           'tick_size': 0.2},
    'IH': {'close_commission_ratio': 2.3e-05,
           'close_commission_today_ratio': 0.0023,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 2.3e-05,
           'tick_size': 0.2},
    'J': {'close_commission_ratio': 6e-05,
          'close_commission_today_ratio': 3e-05,
          'commission_type': COMMISSION_TYPE.BY_MONEY,
          'open_commission_ratio': 6e-05,
          'tick_size': 0.5},
    'JD': {'close_commission_ratio': 0.00015,
           'close_commission_today_ratio': 0.00015,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 0.00015,
           'tick_size': 1.0},
    'JM': {'close_commission_ratio': 6e-05,
           'close_commission_today_ratio': 3e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 6e-05,
           'tick_size': 0.5},
    'JR': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 3.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 1.0},
    'L': {'close_commission_ratio': 2.0,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.0,
          'tick_size': 5.0},
    'LR': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 1.0},
    'M': {'close_commission_ratio': 1.5,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 1.5,
          'tick_size': 1.0},
    'MA': {'close_commission_ratio': 1.4,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 1.4,
           'tick_size': 1.0},
    'ME': {'close_commission_ratio': 1.4,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 1.4,
           'tick_size': 1.0},
    'NI': {'close_commission_ratio': 6.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 6.0,
           'tick_size': 10.0},
    'OI': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 2.0},
    'P': {'close_commission_ratio': 2.5,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.5,
          'tick_size': 2.0},
    'PB': {'close_commission_ratio': 4e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 4e-05,
           'tick_size': 5.0},
    'PM': {'close_commission_ratio': 5.0,
           'close_commission_today_ratio': 5.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 5.0,
           'tick_size': 1.0},
    'PP': {'close_commission_ratio': 5e-05,
           'close_commission_today_ratio': 2.5e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 5e-05,
           'tick_size': 1.0},
    'RB': {'close_commission_ratio': 4.5e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 4.5e-05,
           'tick_size': 1.0},
    'RI': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 2.5,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 1.0},
    'RM': {'close_commission_ratio': 1.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 1.5,
           'tick_size': 1.0},
    'RO': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 2.0},
    'RS': {'close_commission_ratio': 2.0,
           'close_commission_today_ratio': 2.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.0,
           'tick_size': 1.0},
    'RU': {'close_commission_ratio': 4.5e-05,
           'close_commission_today_ratio': 4.5e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 4.5e-05,
           'tick_size': 5.0},
    'SC': {'close_commission_ratio': 20.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 20.0,
           'tick_size': 0.1},
    'SF': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 2.0},
    'SM': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 2.0},
    'SN': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 10.0},
    'SP': {'close_commission_ratio': 5e-05,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 5e-05,
           'tick_size': 2.0},
    'SR': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 1.0},
    'T': {'close_commission_ratio': 3.0,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 3.0,
          'tick_size': 0.005},
    'TA': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 3.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 2.0},
    'TC': {'close_commission_ratio': 4.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 4.0,
           'tick_size': 0.2},
    'TF': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 3.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 0.005},
    'TS': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3,
           'tick_size': 0.005},
    'V': {'close_commission_ratio': 2.0,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.0,
          'tick_size': 5.0},
    'WH': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 1.0},
    'WR': {'close_commission_ratio': 4e-05,
           'close_commission_today_ratio': 4e-05,
           'commission_type': COMMISSION_TYPE.BY_MONEY,
           'open_commission_ratio': 4e-05,
           'tick_size': 1.0},
    'WS': {'close_commission_ratio': 2.5,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 2.5,
           'tick_size': 1.0},
    'Y': {'close_commission_ratio': 2.5,
          'close_commission_today_ratio': 0.0,
          'commission_type': COMMISSION_TYPE.BY_VOLUME,
          'open_commission_ratio': 2.5,
          'tick_size': 2.0},
    'ZC': {'close_commission_ratio': 4.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 4.0,
           'tick_size': 0.2},
    'ZN': {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 5.0},
    "EG": {'close_commission_ratio': 4.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 4.0,
           'tick_size': 1.0},
    "CJ": {'close_commission_ratio': 3.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 3.0,
           'tick_size': 5.0},
    "UR": {'close_commission_ratio': 5.0,
           'close_commission_today_ratio': 5.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 5.0,
           'tick_size': 1.0},
    "NR": {'close_commission_ratio': 10.0,
           'close_commission_today_ratio': 0.0,
           'commission_type': COMMISSION_TYPE.BY_VOLUME,
           'open_commission_ratio': 10.0,
           'tick_size': 5.0},
}

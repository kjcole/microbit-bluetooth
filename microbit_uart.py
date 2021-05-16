#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#  blewtruth.py
#
#  Talk to the BBC micro:bit over Bluetooth
#
#  Copyright 2021 Kevin Cole <ubuntourist@hacdc.org> 2021.05.12
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#

import os
import sys
from   os.path  import expanduser  # Cross-platform home directory finder
from   bluezero import adapter
from   bluezero import microbit
from   bluezero import async_tools

__appname__    = "micro:bit UART"
__module__     = ""
__author__     = "Kevin Cole"
__copyright__  = "Copyright \N{copyleft symbol} 2021"  # OR {copyright sign}
__agency__     = "N-\N{lightning mood} N-tertainments"
__logo__       = "N-\N{lightning mood}-N"
__credits__    = ["Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Kevin Cole"
__email__      = "ubuntourist@hacdc.org"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"


def main():
    _ = os.system("clear")
    print(f"{__appname__} v.{__version__}")
    print(f"{__copyright__} ({__license__})")
    print(f"{__author__}, {__agency__} <{__email__}>")
    print()
 
    local  = "your_pc_bluetooth"  # PC Bluetooth adaptor
    remote = "your_ubit_bluetooth"  # BBC micro:bit Bluetooth adaptor

    ubit = microbit.Microbit(adapter_addr=local,
                             device_addr=remote)

    def goodbye(data):
        print(data)
        ubit.quit_async()
        ubit.disconnect()
        return True

    ubit.connect()
    ubit.subscribe_uart(goodbye)
    ubit.uart = 'Middle C.'

    ubit.run_async()


if __name__ == '__main__':
    main()

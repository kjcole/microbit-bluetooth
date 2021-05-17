#!/bin/bash
#
# setup.sh
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

sudo apt install python3 python3-pip bluez
mkdir -p "`python -m site --user-site`"
pip install --user -r requirements.txt

bt=$(bluetoothctl show    | grep "^Controller "    | cut -f 2 -d " ")
ub=$(bluetoothctl scan on | grep " BBC micro:bit " | cut -d " " -f 3 | uniq)
sed -i s/your_pc_bluetooth/$bt/g   microbit_uart.py
sed -i s/your_ubit_bluetooth/$ub/g microbit_uart.py

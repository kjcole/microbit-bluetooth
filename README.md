
> Open this page at [https://kjcole.github.io/microbit-bluetooth/](https://kjcole.github.io/microbit-bluetooth/)

## Setup

This code depends upon a computer with Bluetooth capabilites, running
Python 3.x, plus the `bluezero` Python package available from the
[Python Package Index (PyPI)](https://pypi.org/project/bluezero/) and
`microbit_uart.py` included in this repository. On Linux,
`bluetoothctl` from the `bluez` package is also helpful.

Upload the **Blocks** code to the micro:bit, and then, in On
https://makecode.microbit.org/ change the Project Settings: Set
Bluetooth to **No Pairing Required**. (This is not very secure, but
the the **JustWorks pairing** just didn't work.) Then upload the
**Blocks** code to your micro:bit.

### Debian-based Linux systems

On Debian-based systems, type the following at the command prompt (`$`):

```
    ./setup.sh
```

That should install all the necessary components and edit
`microbit_uart.py` and substitute the unique addresses for your
hardware into the source code.

### Non-Debian-based systems

If you are not using Debian, Ubuntu, Mint, or other Debian-based Linux
system, you will need install `Python 3`, `pip` and `bluezero`
manually, and then determine the address of your PC's Bluetooth
adapter and the address of your micro:bit Bluetooth adapter. These are
both a series of six 2-digt hexadecimal numbers separated by colons,
e.g.  F1:E2:D3:4C:5B:6A. Edit `microbit_uart.py` and substitute the
two addresses in place of `your_pc_bluetooth` and
`your_ubit_bluetooth`. (Leave the quotes in place.)


## Use as Extension

This repository can be added as an **extension** in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **New Project**
* click on **Extensions** under the gearwheel menu
* search for **https://github.com/kjcole/microbit-bluetooth** and import

## Edit this project ![Build status badge](https://github.com/kjcole/microbit-bluetooth/workflows/MakeCode/badge.svg)

To edit this repository in MakeCode.

* open [https://makecode.microbit.org/](https://makecode.microbit.org/)
* click on **Import** then click on **Import URL**
* paste **https://github.com/kjcole/microbit-bluetooth** and click import

## Blocks preview

This image shows the blocks code from the last commit in master.
This image may take a few minutes to refresh.

![A rendered view of the blocks](https://github.com/kjcole/microbit-bluetooth/raw/master/.github/makecode/blocks.png)

#### Metadata (used for search, rendering)

* for PXT/microbit
<script src="https://makecode.com/gh-pages-embed.js"></script><script>makeCodeRender("{{ site.makecode.home_url }}", "{{ site.github.owner_name }}/{{ site.github.repository_name }}");</script>

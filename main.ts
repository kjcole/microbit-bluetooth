/**
 * Requires a PC running microbit_uart.py. See README.md in Codeberg repository
 */
bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . . # . .
        . # # # .
        # . # . #
        . . # . .
        . . # . .
        `)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # # # .
        . . # . .
        `)
})
let command = ""
basic.showLeds(`
    # . . # #
    # . . # #
    # # # . .
    # . # . .
    # # # . .
    `)
bluetooth.startIOPinService()
bluetooth.startButtonService()
bluetooth.startTemperatureService()
bluetooth.startMagnetometerService()
bluetooth.startUartService()
bluetooth.startAccelerometerService()
basic.forever(function () {
    command = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Fullstop))
    serial.writeLine(command)
    if (command == "Middle C") {
        music.playTone(262, music.beat(BeatFraction.Whole))
        basic.showString("You typed:" + command)
    }
})

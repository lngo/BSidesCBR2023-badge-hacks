# BSidesCBR2023-badge-hacks
Develop new apps for the BSidesCBR 2023 badge

This work provides a CircuitPython firmware for the BSidesCBR 2023 badge. The normal process to compile the CircuitPython firmware for a specific board should be followed. However, the BSidesCBR 2023 badge is not compatible with the firmware of any exsting board, so one needs to tailor the configuration for that badge. 

Just copy the folder bsidescbr_2023 into the path circuitpython/ports/espressif/boards/ to define a new board.

Then run make as follows to build the firmware

make BOARD=bsidescbr_2023

Then burn the firmware to the board as follows

esptool.py --chip esp32s2  --port /dev/ttyACM0 --no-stub  --before=default_reset --after=hard_reset write_flash --flash_mode dio --flash_freq 80m --flash_size detect 0x0000 build-bsidescbr_2023/firmware.bin

The badge shall have circuitpython ENABLED. However, the USB mode is not working yet. One needs to run python via REPL by connecting to the badge's COM port.

A more story of this hack can be found here https://www.longngo.net/making/a-hack-of-the-bsidescbr-2023-conference-badge/

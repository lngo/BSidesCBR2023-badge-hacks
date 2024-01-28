USB_VID = 0x303A
USB_PID = 0x0002
USB_PRODUCT = "bsidescbr_2023"
USB_MANUFACTURER = "bsidescbr"

IDF_TARGET = esp32s2

#CIRCUITPY_USB = 1

CIRCUITPY_ESP_FLASH_MODE = dio
CIRCUITPY_ESP_FLASH_FREQ = 80m
CIRCUITPY_ESP_FLASH_SIZE = 2MB
CIRCUITPY_ESPCAMERA = 0

# Include these Python libraries in firmware.
#FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_RGB_Display
FROZEN_MPY_DIRS += $(TOP)/frozen/adafruit_CircuitPython_ST7735R
FROZEN_MPY_DIRS += $(TOP)/frozen/adafruit_CircuitPython_Display_Text
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_datetime
#FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_framebuf


CIRCUITPY_SSL=0
CIRCUITPY_SSL_MBEDTLS=0
CIRCUITPY_WIFI = 0
CIRCUITPY_WIFI_RADIO_SETTABLE_MAC_ADDRESS = 0
CIRCUITPY_IMAGECAPTURE = 0



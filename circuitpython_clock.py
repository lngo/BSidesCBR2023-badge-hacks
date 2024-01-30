import board
import terminalio
import displayio
import busio
from adafruit_display_text import label
from adafruit_datetime import datetime, date, time
import rtc, time
from adafruit_st7735r import ST7735R

WIDTH = 160+2
HEIGHT = 128+2
COLOR_BLACK= 0x000000
COLOR_WHITE = 0xFFFFFF
COLOR_GRAY = 0x0F0F0F
COLOR_RED = 0x0000FF
COLOR_GREEN = 0x00FF00
COLOR_BLUE = 0xFF0000

# Release any resources currently in use for the displays
displayio.release_displays()

spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
display_bus = displayio.FourWire( spi, command=board.TFT_DC, chip_select=board.TFT_CS, reset=board.TFT_RESET )
display = ST7735R(display_bus, width=WIDTH, height=HEIGHT, colstart=0, rotation=90, bgr=False)

# Make the display context
splash = displayio.Group()
display.show(splash)

#Clear all screen
color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = COLOR_WHITE 
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(WIDTH-6, HEIGHT-6, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = COLOR_BLACK  # Purple
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=3, y=2)
splash.append(inner_sprite)

#to set time manually. 
#TODO: Set time using NTP
set_time = time.struct_time((2023, 10, 22, 12, 30, 0, 0, -1, -1))
print("Setting time to:", set_time)
rtc.RTC().datetime  = set_time


#Show bitcoin
text_area_bitcoin = label.Label(terminalio.FONT, text= "Bitcoin = 47,704 AUD(+0.6%)",background_color = COLOR_BLACK,  color=COLOR_GREEN, x=1, y=120)
splash.append(text_area_bitcoin)

#Show date
text_area_date = label.Label(terminalio.FONT, text= datetime.now().date().isoformat(),background_color = COLOR_BLACK, color=COLOR_BLUE, x=20, y=20, scale= 2)
splash.append(text_area_date)


last_time = time.time()

text_area_time = label.Label(terminalio.FONT, text= datetime.now().time().isoformat(),background_color = COLOR_BLACK,  color=COLOR_RED, x=5, y=60, scale = 3)
splash.append(text_area_time)


#TODO: Better memory management as splash seems to consume a lot of memory.
#This block is not indented as normal Python code because REPL shall auto indent
while True:
new_time = time.time()
if(last_time !=  new_time):
last_time =  new_time
splash.pop()

#Show time
text_area_time = label.Label(terminalio.FONT, text= datetime.now().time().isoformat(),background_color = COLOR_BLACK,  color=COLOR_RED, x=5, y=60, scale = 3)
splash.append(text_area_time)

#Properly indented Python looks as follows
'''
while True:
    new_time = time.time()
    if(last_time !=  new_time):
        last_time =  new_time
        splash.pop()

        #Show time
        text_area_time = label.Label(terminalio.FONT, text= datetime.now().time().isoformat(),background_color = COLOR_BLACK,  color=COLOR_RED, x=5, y=60, scale = 3)
        splash.append(text_area_time)
'''





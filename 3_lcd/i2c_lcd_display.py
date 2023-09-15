
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Initialize the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize the LCD screen
lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2)

# Clear display
lcd.clear()

# Print a two-line message
lcd.message = "Hello\nRaspberry!"
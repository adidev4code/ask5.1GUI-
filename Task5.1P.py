Code:

import tkinter as tk
import lgpio

# LED pin numbers (BCM)
led_pins = {"Red": 17, "Green": 27, "Blue": 22}

# Open GPIO chip
chip = lgpio.gpiochip_open(0)

# Request all pins as output
for pin in led_pins.values():
    lgpio.gpio_claim_output(chip, pin)

# Function to select LED
def select_led():
    chosen = led_choice.get()
    for color, pin in led_pins.items():
        if color == chosen:
            lgpio.gpio_write(chip, pin, 1)
        else:
            lgpio.gpio_write(chip, pin, 0)

# Exit function
def close_app():
    for pin in led_pins.values():
        lgpio.gpio_write(chip, pin, 0)
    lgpio.gpiochip_close(chip)
    window.destroy()

# GUI setup
window = tk.Tk()
window.title("LED Controller")

led_choice = tk.StringVar(value="Red")

for color in led_pins.keys():
    tk.Radiobutton(window, text=color, variable=led_choice, value=color, command=select_led).pack(anchor="w")

tk.Button(window, text="Exit", command=close_app).pack()

window.mainloop()


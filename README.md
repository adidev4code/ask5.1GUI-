# SIT210 - Task 5.1P: Raspberry Pi GUI

## 📌 Overview

This project is part of SIT210 Embedded Systems Development. The objective is to create a simple **graphical user interface (GUI)** on a Raspberry Pi that controls three LEDs (red, green, and blue) using radio buttons.

---

## 🛠 Requirements

### Hardware

* Raspberry Pi with Raspberry Pi OS
* Breadboard
* 3 x LEDs (red, green, blue)
* 3 x 220 Ω resistors
* Jumper wires
* Keyboard, mouse, monitor (for Pi setup)

### Software

* Python 3
* Tkinter (`python3-tk`)
* GPIO control library (`lgpio` recommended, `RPi.GPIO` optional)

---

## ⚡ Hardware Wiring

| LED   | BCM Pin | Physical Pin       | Connection                  |
| ----- | ------- | ------------------ | --------------------------- |
| Red   | GPIO 17 | Pin 11             | GPIO → resistor → LED → GND |
| Green | GPIO 27 | Pin 13             | GPIO → resistor → LED → GND |
| Blue  | GPIO 22 | Pin 15             | GPIO → resistor → LED → GND |
| GND   | -       | Pin 6 (or any GND) | Common ground               |

👉 Always place resistors in series with LEDs.

---

## 🚀 Setup & Installation

1. Update the Raspberry Pi:

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. Install dependencies:

   ```bash
   sudo apt install -y python3-tk python3-lgpio
   ```

   *(For alternate version: `pip3 install RPi.GPIO`)*



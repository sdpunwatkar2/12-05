import time
import pytesseract
from PIL import Image
import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
import threading

target_window_title = "Spotify Free"  # Replace with actual window title
check_interval = 5  # seconds
last_text = ""

def is_window_open(title):
    return any(w.title == title for w in gw.getWindowsWithTitle(title))

def get_window_region(title):
    window = gw.getWindowsWithTitle(title)[0]
    return (window.left, window.top, window.width, window.height)

def capture_text(region):
    screenshot = pyautogui.screenshot(region=region)
    image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return pytesseract.image_to_string(image)

def monitor_window():
    global last_text
    while True:
        if is_window_open(target_window_title):
            region = get_window_region(target_window_title)
            try:
                text = capture_text(region)
                if text.strip() != "":
                    last_text = text.strip()
                    print("\n[✔] Data Receiving:")
                    print("------- OCR TEXT START -------")
                    print(last_text)
                    print("-------- OCR TEXT END --------")
                else:
                    print("[✖] Signal Lost - No data")
            except Exception as e:
                print(f"[✖] An error occurred: {e}")

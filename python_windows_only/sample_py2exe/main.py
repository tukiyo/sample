# http://python.keicode.com/advanced/ctypes-messagebox.php

from ctypes import *

user32 = windll.user32

user32.MessageBoxA(
    0, 
    "Hello, MessageBox!", 
    "Python to Windows API", 
    0x00000040)

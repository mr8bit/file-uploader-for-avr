import sys
import glob
import serial.tools.list_ports

print(serial.tools.list_ports.comports())
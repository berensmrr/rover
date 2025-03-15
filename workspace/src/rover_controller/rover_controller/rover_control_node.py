import serial
import os

class RoverControlNode:
    def __init__(self):
        if os.path.exists('/dev/ttyUSB0'):
            self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        else:
            # Simülasyon durumunda yapılacak işlemler
            print("Simülasyon modunda çalışılıyor, seri port bağlanmadı.")
            self.serial_port = None  # Seri port simülasyonu yapılacak

    def control_rover(self):
        if self.serial_port:
            # Seri port ile iletişim kodu burada olacak
            pass
        else:
            # Simülasyon modunda rovery'i kontrol etme kodu
            print("Simülasyonda rover kontrol ediliyor.")


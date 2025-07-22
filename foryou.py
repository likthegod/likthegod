import math
from turtle import *

# Fungsi untuk menggambar bentuk hati
def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Set kecepatan animasi
speed(9000)

# Set warna latar belakang
bgcolor("black")

# Menggambar bentuk hati
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    color("red")  # Set warna garis

# Menyelesaikan proses menggambar
done()

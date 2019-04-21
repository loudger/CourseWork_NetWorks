import serial

ser = serial.Serial('comnameblyat')

ser.write("Hello world")

x = ser.readline()

print(x)
from serial import Serial
ser = Serial('/dev/ttyACM0', 9600)

def serialWrite(msg):
    ser.write(str.encode(msg))

ser.close()
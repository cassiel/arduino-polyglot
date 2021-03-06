# Test code in Python.

import serial

ser = serial.Serial(port="/dev/tty.usbmodem14171", baudrate=9600, timeout=0.1)

for i in range(20):
    print("[%d]" % i)
    # Send a complete, well-formed message:
    ser.write(bytearray([ord('+') | 0x80,
                         0, 1 & 0xF,
                         0, 10 & 0xF,
                         0x80]))
    ser.flush()

    # This is a simple, protocol-agnostic read: fetch characters until we time out.
    # After a while it should settle down to 0xAB ... 0x80 sequences.
    buf = []
    going = True

    while going:
        bb = ser.read()
        if len(bb) == 0:
            going = False
        else:
            for i in bb:
                if isinstance(i, str): i = ord(i)
                buf.append(i)

    print(''.join((' %02X' % i) for i in buf))

ser.close()

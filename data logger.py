#serial data logger
import serial
import time

#mac - command to find usb port ---> ls /dev/tty* | grep usb
#ser = serial.Serial('/dev/tty.usbmodem11401') #create mac serial object

#windows - use device manager to help find the right COM port
ser = serial.Serial('COM4') #create windows serial object

#clear the serial port
ser.flushInput()

fh = open("data_log.txt","w")
fh.close()

fh = open("timed_data_log.txt","w")
fh.close()

try:
    while True:
        time_tuple = time.localtime() # get struct_time
        time_string = time.strftime("%m/%d/%Y - %H:%M:%S", time_tuple)
        print(time_string)
        ser_bytes = ser.readline()
        decoded_bytes = ser_bytes[0:len(ser_bytes)-2].decode("utf-8")
        print("Hit CTRL-C to exit data logging...")
        fh = open("data_log.txt","a")
        fh.write(decoded_bytes+"\n")
        fh.close()
        fh = open("timed_data_log.txt","a")
        fh.write(time_string + " / " + decoded_bytes+"\n")
        fh.close()
except KeyboardInterrupt:
    print("keyboard interrupt")
    fh.close()

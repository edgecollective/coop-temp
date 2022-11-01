import serial
import datetime
import time
ser=serial.Serial('/dev/ttyACM0')
filename="data.csv"

counter = 0
counter_write = 100 
 
while True:
    out=ser.readline()
    dec=out.decode("utf-8")
    decs = dec.strip().split(",")

    #time=datetime.datetime.now()
    #stamp=datetime.datetime.timestamp(time)*1000
    stamp=int(time.time())
    print(counter, stamp,decs[0],decs[1],decs[2],decs[3])
    counter = counter + 1
    if (counter > counter_write):
        print("writing ...")
        out_str=str(stamp)+","+str(decs[0])+","+str(decs[1])+","+str(decs[2]+","+str(decs[3])+"\n")
        f = open(filename,"a")
        f.write(out_str)
        f.close()
        counter = 0


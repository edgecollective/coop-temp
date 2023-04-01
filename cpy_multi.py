import serial
import datetime
import time
import requests

ser=serial.Serial('/dev/ttyACM2')
#filename="data.csv"


# credentials for belfast.pvos.org (for this particular sensor feed)
#public_key = "i9p7tgvmbxhg"
#private_key = "69cqt4v4hq99"

#keys = [["qeaj3bt3a584","whec2jv525jv"],["834ksnvaq3hn","uas94apvata5"]]
#private_key = "iyxuuqac8gj3"

keys = [["i5y5n4w8dvnp","f6qpqfi5eq3e"]]

# these will stay fixed:
base_url = "http://bayou.pvos.org/data/"
#full_url = base_url+public_key

 
while True:
    
    try:
        out=ser.readline()
        dec=out.decode("utf-8")
        decs = dec.strip().split(",")
        if len(decs)>2:
            feed_id = int(decs.pop(0))
            
            print("-----------------------")
            print("feed_id=",feed_id)
            public_key = "i5y5n4w8dvnp"
            private_key = "f6qpqfi5eq3e"

            full_url = base_url+public_key

            print(public_key,private_key,full_url,"\n")
            
            trailing = decs.pop(-1)
            #print(feed_id,decs)
            N=2
            sensors = [decs[n:n+N] for n in range(0, len(decs), N)]
            print(feed_id,sensors)
            for sensor in sensors:
                if len(sensor)==2:
                    sensorID=sensor[0]
                    temp=sensor[1]
                    print(sensorID,temp)
                    if sensorID=='215':
                        node_id=0
                    if sensorID=='186':
                        node_id=1
                    myobj = {"private_key":private_key, "node_id":node_id,"temperature_c":temp}
                    x = requests.post(full_url, data = myobj)
                    print(myobj) 
                    print(x.text)
                    
            
    except:
        print("error!")
        """
        N=2
        sensors = [decs[n:n+N] for n in range(0, len(decs), N)]
        print(sensors)
        
        for sensor in sensors:
            if len(sensor)==2:
                sensorID=sensor[0]
                temp=sensor[1]
                print(sensorID,temp)
                if sensorID=='215':
                    node_id=0
                if sensorID=='186':
                    node_id=1
                myobj = {"private_key":private_key, "node_id":node_id,"temperature_c":temp}
                x = requests.post(full_url, data = myobj)
                print(myobj) 
                print(x.text)
        except:
            print("error!")
        """     
   

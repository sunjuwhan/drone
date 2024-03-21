from dronekit import connect ,VehicleMode,LocationGlobalRelative,APIException

import time
import socket
import builtins
import math
import argparse


def connectMyCopter():
    pasrser= argparse.ArgumentParser(description="commands")
    pasrser.add_argument("--connect")
    args=pasrser.parse_args()
    
    
    connection_string=args.connect 
    baud_rate=57600
    vehicle=connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle


def arm(vehicle):
    while vehicle.is_armable==False:
        print("Wating for vehicle to become armable....")
        time.sleep(1)
    print("Toooo vehicle is now armable")
    print("**")
    
    vehicle.armed=True
    while vehicle.armed==False:
        print("Wating for drone to become armed")
        time.sleep(1)
    
    
    print("Vehicle is now armed")
    print("OMG props ar oping LOOK out")
    return None


vehicle=connectMyCopter()
arm(vehicle)
print("End of scripts ")
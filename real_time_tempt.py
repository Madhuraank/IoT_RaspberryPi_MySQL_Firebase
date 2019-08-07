
#!/usr/bin/python3
import os
import RPi.GPIO as gpio
import time
import datetime
import glob
import MySQLdb
from time import strftime
import urllib
import urllib.request
from w1thermsensor import W1ThermSensor
from firebase import firebase

sensor = W1ThermSensor() #Get the temperature from your w1 therm sensor
firebase = firebase.FirebaseApplication('https://iot-raspi-d7b60.firebaseio.com/', None)#establish connection to your firebase account


def main():






         while True:

                temperature = sensor.get_temperature()#Your room temp stored to temperature variable
                print("\nThe room  temperature is %s celsius" % temperature)
                time.sleep(1)

                 # Code to write the recorded temperature in the MYSQL database 'templog' and table 'temp-at-interrupt'
                db = MySQLdb.connect(host="192.168.1.6", user="root", passwd="root", db="templog")#get connected to your database

                cur = db.cursor()
                print("connected to db")
                dateWrite = time.strftime("%Y-%m-%d")#get the current date
                timeWrite = time.strftime("%H:%M:%S")#get the current time
                sql = ("""INSERT INTO `temp-at-interrupt` (`date`, `time`, `temperature`) VALUES (%s,%s,%s);""",                             			(dateWrite,timeWrite,temperature)
                
		cur.execute(*sql)
                db.commit()
                print ("Process finished,temperature saved on localhost\n")

         #      db.rollback()
         #      print ("\nProcess Failed to Complete")

                cur.close()
                db.close()


                print("Connecting to firebase")
                if temperature is not None:
                        time.sleep(1)
                        str_temp = ' {0:0.2f} *C '.format(temperature)  

                        print('Temp={0:0.1f}'.format(temperature))      

                else:
                        print('Failed to get reading. Try again!')      
                        time.sleep(5)
                now=datetime.datetime.now()#get the current date
                d=now.strftime("%Y-%m-%d %H:%M:%S")#get the current time
                data = {"temp": temperature,"date & time":d}#room temp, date,time in variable data

                result = firebase.post('tempt',data)#send all the contents of data to tempt field firebase
                print("Process finished,temp saved in firebase")



if __name__== "__main__":


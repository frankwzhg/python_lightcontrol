# this programe will be run backend to collect arduino information and send some comand parameter to arduino

import os   #import socket module to check special ip in this network
import serial, struct   # import function serial
import MySQLdb

db = MySQLdb.connect(host='frankub',
                     user='root',
                     passwd='Dadi4747',
                     db='tango'
                     )
cur = db.cursor()
cur.execute("select ip_address from autocoffe_ipaddressmodel")
ip_list = []
for row in cur.fetchall():
    ip_list.append(row[0])



def detect_ip():
    ser = serial.Serial('/dev/ttyACM2', 9600)

    my_ipaddress = ip_list
    response_list = []
    for ip in my_ipaddress:
        response = os.system("ping -c 1 " + ip)
        response_list.append(response)
    print response_list

    if (0 in response_list):
        print "test"
        ser.write(struct.pack('>2B', 1, 7))
    else:
        ser.write(struct.pack('>2B', 2, 7))


if __name__ == "__main__":
    detect_ip()

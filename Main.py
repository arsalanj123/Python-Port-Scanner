import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('cls', shell=True)

#Welcome and warning
print ("")
print ("Welcome to the Port-scanner")
print ("")
print ("Warning!!! Use at your own discretion!")
#Ask for the starting port and convert to int
print ("")
strstartport = input("Specify the starting port: ")
startport = int(strstartport)


#Ask for the ending port and convert to int
print("")
strendport = input("Specify the ending port: ")
endport = int(strendport)

#Ask for input of remote server
#remoteServer = input("Please enter Remote host to scan: ")
#print = socket.gethost
#remoteServerIP = socket.gethostbyname(remoteServer)

#Ask for ip address range from start to end
firstip = input("Specify the first ip: ")
secondip = input("Specify the second ip: ")

#Convert to str for printing
#startip = int(strstartip)
#endip = int(strendip)

#Clear the screen again
subprocess.call('cls', shell=True)

#Print a nice banner with information on which host we are about to scan
#print ("-" * 60)
#print ("Please Wait! scanning the remote host", remoteServerIP)
#print ("-" * 60)

#Check what time the scan started
t1 = datetime.now()

#intstartip = int(strstartip)
#intendip = int(strendip)

# Iterating over ports and running scanning each port
# error handling is done also

#Iterations
try:
    for ipaddress in (firstip, secondip):
        remoteServerIP = socket.gethostbyname(ipaddress)
        print ("-" * 60)
        print ("Scanning: " + ipaddress)
        print ("-" * 60)
        for port in range(startport, endport):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            strport = str(port)
            if result == 0:
                print ("Port {}: " + strport + " is open")
            sock.close()

#Error handing:

except KeyboardInterrupt:
    sys.exit("You Pressed Ctrl+C")

except socket.gaierror:
    sys.exit("Hostname could not be resolved. Exiting")

except socket.error:
    sys.exit("Could'nt connect to server")

#Check time again
t2 = datetime.now()

#Calculate time difference of time for seeing the duration of port scan
totaltime = t2-t1

#Printing the information to screen
print ("Scanning completed in: ", totaltime)


#modules
#install uing pip package manager 
#example pip install socket
import os
import socket
import subprocess as sp 
import re
os.system("clear")
# regex for ip and port validation
ip_add_pattern_C = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$") 
ip_add_pattern_B = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).$") 
ip_add_pattern_A = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).$") 
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
print('Wait or Press Ctrl+Z to Terminate\n') 

class Dwarf_nmap:
    def __init__(self,iP_Address):
        self.iP_Address=iP_Address
        self.open_ports=[]  
    #function for port checker 
    def port_checker(self,port_min,port_max):
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((self.iP_Address,port))
                    self.open_ports.append(port)
            except:
                pass
        return self.open_ports
    #function for Ip Range finder
    def Ip_range_finder(self,case):  
            ip_addr=".".join(self.iP_Address.split(".",4)[:3])+"."#print first three class in IP 192.168.10.
            #two int operation
            if case == 2:
                for empty in range(255):
                    for i in range(255):
                        ip_add=ip_addr+str(empty)+"."+str(i)
                        s,r=sp.getstatusoutput("ping -c1 -w2 " + ip_add) 
                        if s==0: 
                            print(ip_add+" is UP ✓ ") 
                        else: 
                            pass
            #three int operation
            if case == 3:
                for i in range(255):
                        ip_add=ip_addr+str(i)
                        s,r=sp.getstatusoutput("ping -c1 -w2 " + ip_add) 
                        if s==0: 
                            print(ip_add+" is UP ✓ ") 
                        else: 
                            pass
            #four int operation
            if case == 4:
                start=int(self.iP_Address.split(".",4)[3])
                for i in range(start,255):
                        ip_add=ip_addr+str(i)
                        s,r=sp.getstatusoutput("ping -c1 -w2 " + ip_add) 
                        if s==0: 
                            print(ip_add+" is UP ✓ ") 
                        else: 
                            pass
            
# ip and port validator to avoid error
class Validator:
    def __init__(self,iP_Address):
        self.iP_Address=iP_Address
    def ip_valid(self):
        while True:
            if self.iP_Address.count('.')==1 :
                return 0
            elif self.iP_Address.count('.')==2  and ip_add_pattern_A.search(self.iP_Address):
                    return 2
            elif self.iP_Address.count('.')==3 and ip_add_pattern_B.search(self.iP_Address):
                    return 3
            elif ip_add_pattern_C.search(self.iP_Address):
                    return 4
            else:
                return 0
    #port validation input like 90-100 
    #this func check and give like 90 and 100
    def port_valid(self):
        while True:
            P_list=[]
            f_list=[0]
            port_range_valid = port_range_pattern.search(self.iP_Address.replace(" ",""))
            if port_range_valid:  
                P_list.append(1)
                P_list.append(int(port_range_valid.group(1)))
                P_list.append(int(port_range_valid.group(2)))
                if(P_list[1]+1>P_list[2]):
                    return f_list
                return P_list
            return f_list
            # send list of ports
#intro of the function
def intro():
    print(
        '''
        [0] Find ip Address Range
        [1] Find Open-port in Ipaddress
        '''
    )
    while True:
        try:
            Choice=int(input("[0-1] : "))
            if Choice in [0,1]:
                return Choice
        except:
            print("Enter Valid Option String not Acceptable")
            continue
# To check the ip and port health like validator
def check_ip_health(choice):
    address=[]
    while True:
        if(int(choice)) :
            print("For port Range Enter like 10.10.168.89")
        else:
            print("For iP Address Range Enter like 10.10.* or 10.10.168.* or [10.10.168.89 it find range btw 89 to 255]")    
        ip_Adderess=input("Enter Ip-Address : ").replace('*','')
        valid=Validator(ip_Adderess)
        #func for port choice
        def func_choice():
            while True:
                print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120) not Same Range ")
                port_range = input("Enter port range: ")
                valid=Validator(port_range)
                if valid.port_valid()[0] == 1:
                    return valid.port_valid()[1:]
                continue 
        #if ip address fail it avoid errors    
        if valid.ip_valid()==0 or int(choice) and valid.ip_valid()==3:
            if int(valid.ip_valid()):
                print("You Entered invalid Ip-address Try Again..\n")
            print("Enter Ip-address like 192.168.10.10 or <int>[0-255].<int>[0-255].<int>[0-255].<int>[0-255]")
            continue
        else:
            if int(choice):
                address.append(ip_Adderess)
                return address+func_choice()# send list with ipaddress + ports
            address.append(ip_Adderess)
            address.append(valid.ip_valid())
            return address# send list with ipaddress + number of class


def main():
    Choice=intro()
    ip_Adderess=check_ip_health(Choice)
    search=Dwarf_nmap(ip_Adderess[0])
    os.system("clear")
    if int(Choice):
        print("TARGET :"+ip_Adderess[0])
        print("\nScanning...\n")
        for port in search.port_checker(ip_Adderess[1],ip_Adderess[2]):
            print(f'port {port} is open on {ip_Adderess[0]}.')
        print("\n")
    else:
        print("\nScanning...\n")
        search.Ip_range_finder(ip_Adderess[1])

# Driver code
if __name__ == "__main__":
	main()


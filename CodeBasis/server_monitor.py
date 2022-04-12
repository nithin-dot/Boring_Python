from ipaddress import ip_address
import os 
import subprocess as sp 
import re
os.system("clear")
ip_add_pattern_C = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$") 
ip_add_pattern_B = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).$") 
ip_add_pattern_A = re.compile("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]).$") 
print('Wait or Press Ctrl+Z to Terminate\n') 


def port_checker():
    while True:
        ip_address=input("Enter the Ip Address : ")
        if ip_add_pattern_C.search(ip_address):
            print(f"{ip_address} is a valid ip address")
            break


def Ip_range_finder():
        def class_A(A_IP,A_value):
            for i in range(255):
                ip=A_IP+str(i) 
                s,r=sp.getstatusoutput("ping -c1 -w2 " + ip) 
                if s==0: 
                    print(ip+" is UP ✓ ") 
                else: 
                    pass 
        while True:
            ip_address='10.10.110.*'
            if ip_address.count('.')==1:
                print("Enter IP-Address like 10.10.* or 10.10.100.*")
                continue
            elif ip_address.count('.')==2:
               if  ip_add_pattern_A.search(ip_address[:-1]):
                    print(f"{ip_address} is a valid ip address")
                    break
            elif ip_address.count('.')==3:
                if ip_add_pattern_B.search(ip_address[:-1]):
                    print(f"{ip_address} is a valid ip address")
                    break
        striped_IP=ip_address[:-2]
        print(striped_IP)
        class_A(str(striped_IP+'.'),int(striped_IP[-3:]))
        # ip_Class=ip_address.count('.')
        # print(ip_Class)
       
def main():
    print(
        '''
        [1] Find ip Address Range
        [2] Find Open-port in Ipaddress
        '''
    )
    while True:
        try:
            Choice=int(input("[1-2] : "))
            if Choice in [1,2]:
                break
        except:
            print("Enter Valid Option String not Acceptable")
            continue
    if Choice==1:
        Ip_range_finder()
    else:
        port_checker()

# Driver code
if __name__ == "__main__":
	main()


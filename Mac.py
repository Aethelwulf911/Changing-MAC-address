# BOUSSOURA Mohamed Cherif , Boufarik-Blida-ALGERIA , 5:30 pm 04-12-2020

# This code run with Python3
# I used vscode after i create a venv : python3 -m venv venv
# i activated it : source venv/bin/activate
# these command used in CMD : 
# ifconfig eth0 down
# ifconfig eth0 hw ether **:**:**:**:**:**
# ifconfig eth0 up

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ code ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import subprocess,re

class MAC_Changer:
    def __init__(self):
        self.MAC=""
    
    def get_MAC(self,iface):
        # ifconfig
        
        output = subprocess.run(["ifconfig",iface],shell=False,capture_output=True)
        
        cmd_result = output.stdout.decode('utf-8')
        
        # get the MAC adresse
        
        pattern = 'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        
        regex = re.compile(pattern)
        
        ans = regex.search(cmd_result)

        current_mac = ans.group().split(" ")[1]

        self.MAC = current_mac

        return current_mac

    def change_mac(self,iface,new_mac):
        
        print("[*] The current MAC address is "+self.get_MAC(iface))
        
        # ifconfig eth0 down
        
        output = subprocess.run(["ifconfig",iface,"down"],shell=False,capture_output=True)
        
        # ifconfig eth0 hw ether 00:11:22:33:44:55
        
        output = subprocess.run(["ifconfig",iface,"hw","ether",new_mac],shell=False,capture_output=True)
        
        # ifconfig eth0 up
        
        output = subprocess.run(["ifconfig",iface,"up"],shell=False,capture_output=True)
        
        # done !
        
        print("[*] Updated MAC adress is "+self.get_MAC(iface))

        return self.get_MAC(iface)
         
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_-$$-_~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ help ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# if you don't understand how i wrote this regular expression (REGEX) just copy your text from cmd (ifconfig)
# after test my expression in this website : https://pythex.org/
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_-$$-_~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

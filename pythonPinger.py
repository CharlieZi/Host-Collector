import socket
import time

def hostGettor(domainName):
    hostIP = socket.gethostbyname(domainName)
    return hostIP

with open("hostTargetList","r") as file:
    domainList =  file.readlines()
    with open("hostIPScanResult","w+") as hostfile:
        
        updateTime = ["# Updated at %s\n\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),]

        hostList = [] + updateTime


        for domain in domainList:
            domain = domain.replace("\n","")
            hostIP = hostGettor(domain)
            hostList.append("%s\t%s\n"%(domain,hostIP))

        hostfile.writelines(hostList)
            
print "done!"

            
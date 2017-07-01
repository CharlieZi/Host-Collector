#! /usr/bin/env python
import socket
import time


def hostGettorFromGoogleDNS(domainName):
    import dns.resolver
    Gresolver = dns.resolver.Resolver()
    Gresolver.nameservers = ['203.196.0.6']
    answers = Gresolver.query(domainName)
    for rdata in answers:
        hostIP = rdata
    return hostIP



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
            try:
                hostIP = hostGettorFromGoogleDNS(domain)
            except:
                break
            hostList.append("%s\t%s\n"%(domain,hostIP))

        hostfile.writelines(hostList)
            
print "done!"

            

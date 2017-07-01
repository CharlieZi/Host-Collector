#!/usr/bin/env python

import dns.resolver
import time

def hostGetFromGDns(domain):
    myresolver = dns.resolver.Resolver(configure=False)
    myresolver.nameservers = ['8.8.8.8']
    result = myresolver.query(domain,'a',tcp=True,)
    for hostIP in result:
        return hostIP 
        break

print hostGetFromGDns("tumblr.com")

with open("hostTargetList","r") as file:
    domainList =  file.readlines()
    with open("hostIPScanResult111","w+") as hostfile:       
        updateTime = ["# Updated at %s\n\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),]
        hostList = [] + updateTime
        for domain in domainList:
            domain = domain.replace("\n","") 
            try:
                hostIP = hostGetFromGDns(domain)
            except:
                break
            hostList.append("%s\t%s\n"%(domain,hostIP))
        hostfile.writelines(hostList)
print "done!"

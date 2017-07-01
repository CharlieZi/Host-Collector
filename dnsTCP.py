#!/usr/bin/env python

import dns.resolver

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
    for domain in domainList:
        domain = domain.replace("\n","") 
        try:
            hostIP = hostGetFromGDns(domain)
            print hostIP
        except:
            break
            
print "done!"
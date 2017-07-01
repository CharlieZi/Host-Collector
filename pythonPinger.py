#! /usr/bin/env python
import socket
import time
import urllib2
import os
from dns import resolver
import subprocess

def checkConnState(IPString):
    
    ping = subprocess.Popen(
        ["ping", "-c", "1", "-s", "1", "-W", "1", "%s"%(IPString)],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    pingState = ping.communicate()[0].split(",")[-1].split("%")[0].split(" ")[-1]
    if pingState == "0.0":
        return True
    else:
        return False



def hostGettorFroDNS(DNSServerIP,domainName):

    Gresolver = resolver.Resolver()
    Gresolver.nameservers = [DNSServerIP]
    answers = Gresolver.query(domainName,tcp=True)
    for rdata in answers:
        hostIP = rdata
    return hostIP

print hostGettorFroDNS("8.8.8.8","tumblr.com")


def hostGettor(domainName):
    hostIP = socket.gethostbyname(domainName)
    return hostIP

def DNSswitch(domain):
    with open("DNSList","r") as file:
        dnslist = file.readlines()
        countNum = 0
        for dns in dnslist:
            dns = dns.replace("\n","")
            print dns
            try:
                hostIP = hostGettorFroDNS(dns,domain)
                print countNum
                countNum += 1
                if checkConnState(hostIP):
                    return [hostIP,dns]
                    break
                else:
                    print "fail dns %s"%(dns)
                    pass

            except:
                print "fail dns %s"%(dns)
                pass
            


# print DNSswitch("google.com")


# test = hostGettorFroDNS("114.114.114.114","baidu.com")
# print test
# print checkConnState(test)


# def main():

# with open("hostTargetList","r") as file:
#     domainList =  file.readlines()
#     with open("hostIPScanResult","w+") as hostfile:
        
#         updateTime = ["# Updated at %s\n\n"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),]
#         hostList = [] + updateTime
#         domainNum = 0
#         for domain in domainList:
#             domainNum += 1
#             print "%s/%s"%(domainNum,len(domainList))
            
#             domain = domain.replace("\n","") 
#             try:
#                 hostIP = hostGettorFroDNS("114.114.114.114",domain)
#                 print checkConnState(hostIP)
#             except:
#                 break
#             hostList.append("%s\t%s\n"%(domain,hostIP))
#         hostfile.writelines(hostList)
            
# print "done!"


# if __name__ == "__main__":
#     main()
            

# line = "http://114.114.114.114"
# result = list()
# try:
#     response = urllib2.urlopen(line,timeout=4)
#     print response
#     result.append(line)                            
#     result.sort()
# except urllib2.HTTPError, e:
#     print e.code
# except:
#     print "error"

# import subprocess
# ping = subprocess.Popen(
#     ["ping", "-c", "1", "-s", "1", "-W", "1", "192.168.1.1"],
#     stdout = subprocess.PIPE,
#     stderr = subprocess.PIPE
# )
# out,error = ping.communicate()
# print out





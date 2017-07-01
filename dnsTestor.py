import dns.resolver

my_resolver = dns.resolver.Resolver()

# 8.8.8.8 is Google's public DNS server
my_resolver.nameservers = ['8.8.8.8']

answers = my_resolver.query('mx.tumblr.com')
print answers.rdata

for rdata in answers:
    print rdata
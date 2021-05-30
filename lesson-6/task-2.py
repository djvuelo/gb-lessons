IPs_requests = {}
spammer = {'IP': '', 'requests': 0}
with open('files/nginx_logs.txt', 'r') as logs:
    for log in logs:
        IP = log.split(' - - ')[0]
        count_request = IPs_requests.setdefault(IP, 0)
        IPs_requests[IP] += 1
        if spammer['requests'] < IPs_requests[IP]:
            spammer['IP'] = IP
            spammer['requests'] = IPs_requests[IP]

print(spammer)
print(len(IPs_requests))

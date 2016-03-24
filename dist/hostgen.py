#/usr/bin/env python

import sys, socket, struct

def ips(start, end):
    start = struct.unpack(">I", socket.inet_aton(start))[0]
    end = struct.unpack(">I", socket.inet_aton(end))[0]
    return [socket.inet_ntoa(struct.pack(">I", i)) for i in range(start, end)]

hosts = ips(sys.argv[1], sys.argv[2])

with open ('hosts', 'a') as f:
    for line in hosts:
        f.write("{}\n".format(line))

print("Done.")


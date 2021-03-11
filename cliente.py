import rpyc
import sys
import os
import time

start = time.time()

if len(sys.argv) < 2:
    exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]
vetor = []
for i in range(int(sys.argv[2])):
    vetor.append(i)

conn = rpyc.connect(server,18861)
rpyc.discover("MY")


print("resultado soma: ", conn.root.soma_vetor(vetor))

end = time.time()
print("tempo cliente: ", end-start)
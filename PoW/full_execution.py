#!/usr/bin/env python3

import subprocess
import time
import sys
import csv

#Argon 2 Parameter values:
argon2iterations=[1, 100, 1000]
argon2memory=[1024, 4096, 8192]
argon2parallelism=[1, 8, 16]

#Catena Parameter values:
catenagarlic=[15, 21, 22]

#Yescrypt Parameter values:
yescryptblocks=[1024, 4096, 8192]
yescryptblocksize=[8, 32, 64]
yescryptparallelism=[1, 8, 16]

#Creation and setup of the .csv output file with execution times:
with open('pow_execution.csv', mode='w') as execution_file:
    execution_writer = csv.writer(execution_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    execution_writer.writerow(['Argon 2i 10 iterations 1024 KB 1 thread', 'Argon 2i 100 iterations 4096 KB 8 threads', 'Argon 2i 500 iterations 8192 KB 16 threads','Catena garlic 15','Catena garlic 18','Catena garlic 20','Yescrypt 1024 blocks blocksize 8 1 thread','Yescrypt 2048 blocks blocksize 32 8 threads','Yescrypt 4096 blocks blocksize 64 16 threads'])

if len(sys.argv) > 2:
    print ("Usage: python full_execution.py (iterations)")
    exit()
if len(sys.argv) == 2:
    num_iterations = sys.argv[1]
else:
    num_iterations = 1

for i in range(0, int(num_iterations)):
    #****************ARGON2****************
    ellapsed=['0']
    #Argon 2i 10 iterations 1024 KB 1 thread
    start_time = time.time()
    subprocess.run('echo -n "password" | ./argon2/argon2 somesalt -i -t 10 -k 1024 -p 1 -l 32', shell=True) 
    ellapsed[0]=(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[0])

    #Argon 2i 100 iterations 4096 KB 8 threads
    start_time = time.time()
    subprocess.run('echo -n "password" | ./argon2/argon2 somesalt -i -t 100 -k 4096 -p 8 -l 32', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[1])

    #Argon 2i 500 iterations 8192 KB 16 threads
    start_time = time.time()
    subprocess.run('echo -n "password" | ./argon2/argon2 somesalt -i -t 500 -k 8192 -p 16 -l 32', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[2])

    #****************CATENA****************
    #Catena garlic 15
    start_time = time.time()
    subprocess.run('./catena/catena-Butterfly-blake2b-test_vectors password somesalt somesalt 15', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[3])

    #Catena garlic 18
    start_time = time.time()
    subprocess.run('./catena/catena-Butterfly-blake2b-test_vectors password somesalt somesalt 18', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[4])

    #Catena garlic 20
    start_time = time.time()
    subprocess.run('./catena/catena-Butterfly-blake2b-test_vectors password somesalt somesalt 20', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[5])

    #****************YESCRYPT****************
    #Yescrypt 1024 blocks blocksize 8 1 thread
    start_time = time.time()
    subprocess.run('./yescrypt/tests password somesalt YESCRYPT_DEFAULTS 1024 8 1 0 0 64', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[6]) 

    #Yescrypt 2048 blocks blocksize 32 8 threads
    start_time = time.time()
    subprocess.run('./yescrypt/tests password somesalt YESCRYPT_DEFAULTS 2048 32 8 0 0 64', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[7])

    #Yescrypt 4096 blocks blocksize 64 16 threads
    start_time = time.time()
    subprocess.run('./yescrypt/tests password somesalt YESCRYPT_DEFAULTS 4096 64 16 0 0 64', shell=True)
    ellapsed.append(time.time() - start_time)
    print ("Ellapsed time: " , ellapsed[8])

    with open('pow_execution.csv', mode='a') as execution_file:
        execution_writer = csv.writer(execution_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        execution_writer.writerow([ellapsed[0], ellapsed[1], ellapsed[2], ellapsed[3], ellapsed[4], ellapsed[5], ellapsed[6], ellapsed[7], ellapsed[8]])

print("-----------------------------------------------------------")
print("End of execution")

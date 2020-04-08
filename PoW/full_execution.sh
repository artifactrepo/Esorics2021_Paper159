#!/bin/bash

#Coloring variables:
RED='\033[0;31m' # Red color
GREEN='\e[38;5;82m'
NC='\033[0m' # No Color

#Execution parameters:
executioniterations=1
if [ "$#" -eq 1 ]; then
	echo "param 1: $1"
	executioniterations=$1
fi

if [ "$#" -gt 1 ]; then
	echo "Usage: 'bash full_execution (iterations)'"
	exit
fi

#Argon 2 Parameter values:
argon2mode='-i -d'
argon2iterations='1 3 10 100 256'
argon2memory='1024 2048 4096'
argon2parallelism='1 2 4'

#Catena Parameter values:
catenamode='catena-Butterfly-blake2b-test_vectors catena-Dragonfly-blake2b-test_vectors'
catenagarlic='1 3 5 10 15 20 21 22'

#Yescrypt Parameter values:
yescryptblocks='128 256 512 1024 2048 4096 8192'
yescryptblocksize='8 16 32'
yescryptparallelism='1 2 4'

 
echo -e "{$RED}PoW for VM Detection execution script $NC"
echo "-----------------------------------------------------------"
echo

for (( it=0; it<$executioniterations; it++ ))
do
	echo -e "Beginning Argon2 hashing algorithm executions (press Enter to continue)"
	read nothing
	#Execution loop for Argon2:
	for mode in $argon2mode 
	do
		for iterations in $argon2iterations
		do
			for memory in $argon2memory
			do
				for parallelism in $argon2parallelism
				do
					echo -e "${GREEN}time echo -n 'password' | ./argon2/argon2 somesalt $mode -t $iterations -k $memory -p $parallelism -l 32 $NC"
					time echo -n 'password' | ./argon2/argon2 somesalt $mode -t $iterations -k $memory -p $parallelism -l 32
					echo
				done
			done
		done
	done
	echo
	echo -e "${RED}End of Argon2 hashing algorithm executions $NC"
	echo "-----------------------------------------------------------"
	echo
	echo -e "Beginning Catena hashing algorithm executions (press Enter to continue)"
	read nothing
	
	#Execution loop for Catena:
	for mode in $catenamode
	do
		for garlic in $catenagarlic
		do
			echo -e "${GREEN}time ./catena/$mode password somesalt somesalt $garlic $NC"
			time ./catena/$mode password somesalt somesalt $garlic
		done
	done
	echo
	echo -e "${RED}End of Catena hashing algorithm executions $NC"
	echo "-----------------------------------------------------------"
	echo
	echo -e "Beginning Yescrypt hashing algorithm executions (press Enter to continue)"
	read nothing
	
	#Execution loop for Yescrypt:
	for blocks in $yescryptblocks
	do
		for blocksize in $yescryptblocksize
		do
			for parallelism in $yescryptparallelism
			do
				echo -e "${GREEN}time ./yescrypt/tests password somesalt YESCRYPT_DEFAULTS $blocks $blocksize $parallelism 0 0 64 $NC"
				time ./yescrypt/tests password somesalt YESCRYPT_DEFAULTS $blocks $blocksize $parallelism 0 0 64
			done
		done
	done
	echo
	echo -e "${RED}End of Yescrypt hashing algorithm executions $NC"
	echo "-----------------------------------------------------------"
	echo
done
echo -e "End of Hashing algorithms execution (press Enter to finish)"
read nothing

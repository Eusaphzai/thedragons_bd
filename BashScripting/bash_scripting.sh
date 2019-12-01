#!/bin/bash

#Hello World
echo "Hello World"

#Bash and run the file
chmod a+x First.sh
./First.sh

#multi-line comment
: '
The following script calculates
the square value of the number, 5.
'
((area=5*5))
echo $area

#While-loop
valid=true
count=1
while [ $valid ]
do
echo $count
if [ $count -eq 5 ];
then
break
fi
((count++))
done

#for-loop
for (( counter=10; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"

#Get User Input
echo "Enter Your Name"
read name
echo "Welcome $name to LinuxHint"


#Using if statement with AND logic
echo "Enter username"
read username
echo "Enter password"
read password
if [[ ( $username == "admin" && $password == "secret" ) ]]; then
echo "valid user"
else
echo "invalid user"
fi

#Using if statement with OR logic
echo "Enter any number"
read n
if [[ ( $n -eq 15 || $n  -eq 45 ) ]]
then
echo "You won the game"
else
echo "You lost the game"
fi

#Add two numbers
echo "Enter first number"
read x
echo "Enter second number"
read y
(( sum=x+y ))
echo "The result of addition=$sum"

#Create a Function
function F1()
{
echo 'I like bash programming'
}
F1

#Read a file
file='book.txt'
while read line; do
echo $line
done < $file

#Delete a File
echo "Enter filename to remove"
read fn
rm -i $fn

#Start Zookeeper
T1=$(jps | grep QuorumMainPeer)
if ($T1) 
then
echo “Zookeeper is not running”
echo “Zookeeper starting...”
cd ~/kafka
./bin/zookeeper-server-start.sh config/zookeeper.properties
else
echo “Zookeeper is running”
fi

#Stop Zookeeper
if ($T1) 
then
echo “Zookeeper is running”
echo “Zookeeper stopping...”
cd ~/kafka
./bin/zookeeper-server-stop.sh config/zookeeper.properties
else
echo “Zookeeper is running”
fi


#Start Kafka
T1=$(jps | grep QuorumMainPeer)
if ($T1) 
then
echo “kafka is not running”
echo “kafka starting...”
cd ~/kafka
./bin/kafka-server-start.sh config/server.properties
else
echo “Kafka is running”
fi

#Start Kafka
T1=$(jps | grep QuorumMainPeer)
if ($T1) 
then
echo “kafka is running”
echo “kafka stopping...”
cd ~/kafka
./bin/kafka-server-stop.sh config/server.properties
else
echo “Kafka is running”
fi

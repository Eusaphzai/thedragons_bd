# Q1: Create a list, Then, fill it with 30 random numbers
import random

# l = random.sample(range(1,30), 1)
# print(l)

# num = 30
# start = 0
# end = 30
# print(Rand(start, end, num)) 

my_randoms = []
for i in range (30):
    my_randoms.append(random.randrange(1,101,1))

print (my_randoms)
#=======================================================================================================

# Q2: Create method (in a class) that returns the name, and id of the Instance of the object.
class Person:
  def __init__(self, name, id):
    self.name = name
    self.id = id

p1 = Person("Asad Khan", 10)

print(p1.name)
print(p1.id)
#=======================================================================================================
# Q3: Given an integer array, find the smallest missing positive integer.
# ifilterfalse
from itertools import count, filterfalse 

A = [1,14,2,5,3,7,8,12]
print(next(filterfalse(set(A).__contains__, count(1))))

# Array
# def solution(A): 
  
    # Assigning maximum value to a variable
    # m = max(A)  
    # if m < 1: 
          
        # In case all values in our array are negative 
        # return 1 
    # if len(A) == 1: 
          
        # If it contains only one element 
        # return 2 if A[0] == 1 else 1     
    # l = [0] * m 
    # for i in range(len(A)): 
        # if A[i] > 0: 
            # if l[A[i] - 1] != 1: 
                  
                # Changing the value status at the index of our list 
                # l[A[i] - 1] = 1 
    # for i in range(len(l)): 
          
        # Encountering first 0, i.e, the element with least value 
        # if l[i] == 0:  
            # return i + 1
            # In case all values are filled between 1 and m 
    # return i + 2     
  
# A = [0, 10, 2, -10, -20] 
# print(solution(A)) 
#=================================================================================
# Q4: Remove duplicates

weekdays = ["sun", "mon", "tue", "sun", "mon", "tue", "wed", "thu", "fri", "wed", "thu", "fri", "sat"]
print ("The original list is : " +  str(weekdays))

res = [i for n, i in enumerate(weekdays) if i not in weekdays[:n]]
print ("The list after removing duplicates : " + str(res))
#=======================================================================================================

# Q5: Read a file in python

import csv  
with open('shakespeare.txt') as csv_file:  
    csv_reader = csv.reader(csv_file, delimiter=',')  
    line_count = 0  
    for row in csv_reader:  
        if line_count == 0:  
            print(f'Column names are {", ".join(row)}')  
            line_count += 1 
#=======================================================================================================  
#  a. Read a file in scala

# import scala.io.Source

# val filename = "fileopen.scala"
# for (line <- Source.fromFile(filename).getLines) {
#   println(line)
# }

# import java.io._

# object Demo {
#    def main(args: Array[String]) {
#       val writer = new PrintWriter(new File("test.txt" ))

#       writer.write("Hello Scala")
#       writer.close()
#    }
# }
#=======================================================================================================
# Q6: Write csv in python

data = [{'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'},   
{'Rank': 'A', 'first_name': 'Smith', 'last_name': 'Rodriguez'},  
{'Rank': 'C', 'first_name': 'Tom', 'last_name': 'smith'},  
{'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'},   
{'Rank': 'A', 'first_name': 'Alex', 'last_name': 'Tim'}]  
import csv  
   
with open('Python.csv', 'w') as csvfile:  
    fieldnames = ['first_name', 'last_name', 'Rank']  
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
   
    writer.writeheader()  
    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})  
    writer.writerow({'Rank': 'A', 'first_name': 'Smith',  
                     'last_name': 'Rodriguez'})  
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})  
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})  
   
print("Writing complete")
#======================================================================================================= 
# a. Write csv in scala
scala> val f = new File("out.csv")

scala> val writer = CSVWriter.open(f)
writer: com.github.tototoshi.csv.CSVWriter = com.github.tototoshi.csv.CSVWriter@783f77f1

scala> writer.writeAll(List(List("a", "b", "c"), List("d", "e", "f")))

scala> writer.close()



#=======================================================================================================

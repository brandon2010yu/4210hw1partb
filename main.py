# -------------------------------------------------------------------------
# AUTHOR: Brandon Yu
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to
# work here only with standard vectors and arrays

# importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes  # representing the most specific possible hypothesis
print(hypothesis)

# find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here
print("First positive training data in db: ")
for positive in db:
    if positive[4] == 'Yes':
        hypothesis = [positive[0], positive[1], positive[2], positive[3]]
        print(hypothesis)
        break

# find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis
# (special characters allowed: "0" and "?") #--> add your Python code here
for find in db:

    if find[4] == 'Yes':

        if find[0] != hypothesis[0]:
            hypothesis[0] = '?'

        if find[1] != hypothesis[1]:
            hypothesis[1] = '?'

        if find[2] != hypothesis[2]:
            hypothesis[2] = '?'

        if find[3] != hypothesis[3]:
            hypothesis[3] = '?'



print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)

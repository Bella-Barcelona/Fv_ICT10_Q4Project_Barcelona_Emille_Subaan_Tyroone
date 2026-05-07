from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

import logging
logging.getLogger('matploblib').setLevel(logging.ERROR) # to make sure that no error message are shown

class Graph: 
    def __init__(self, Day, Attendance):  #to make a class for out attendances and days
        self.Day = Day
        self.Attendance = Attendance

plt.figure()
plt.plot([0,1], [0,1])
plt.close() # to make the graph grided and to make sure that it is shown
Day =[]
Attendance = []# empty lists so we can store our data
 
def Add(e):
    name = document.getElementById("Week").value#getting the values from index
    attendance = document.getElementById("Absent").value

    graph = Graph(name, attendance)# creating an object for the graph
    Day.append(name) #adding this to the list
    Attendance.append(attendance) 
    attendance_array = np.array(Attendance, dtype=float)# converting attendance into a numpy array so we can plot, dtype for the data type specifications to make it easier

    plt.clf()
    plt.figure()
    plt.plot(Day, attendance_array, marker='o', color='pink')# plotting the graph
    plt.title("Attendance Chart")
    plt.xlabel("Day")
    plt.ylabel(" Attendance")
    plt.grid(True)# all the design details for the graph
    
    document.getElementById("output").innerHTML = "" #makes sure that the graph is shown only once
    display(plt.gcf(), target="output")
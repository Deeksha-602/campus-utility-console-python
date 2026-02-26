from collections import deque
import copy
import csv
import json
from logging import exception
import logging
import platform
import re
import socket
import sys
import threading
import os
 
# -------------------------------------------------
# ---------------- Declarations -------------------
# -------------------------------------------------


courses = ["CS101", "MA102"]
students = [(1, "Aman"), (2, "Riya")]
faculty = {"Dr.Sharma", "Dr.Khan"}
id_name = {1: "Aman", 2: "Riya"}
data = {
    "dept": "CSE",
    "students": ["A", "B"]
}
students_detail = [(1, "Ria"), (2, "Aman"), (3, "kunal")]
 
 
lock = threading.Lock()


# -------------------------------------------------
# -------- Task 15 & 16 GLOBAL TRACKER -----------
# -------------------------------------------------

features_ran = set()
created_files = set()
debug_enabled = False
 

#================================================== 
#-----------Task:1 --------------------------------
#==================================================


def python_info():
   print("\n--------------------------------------------------")
   print("Python Version:", sys.version)
   print("Implementation:", platform.python_implementation())
   name = "Campus"
   print(f"Welcome to {name} Ulity Console!\n")
   print("--------------------------------------------------\n")
   features_ran.add("Python Info")
 

#===============================================================================
#-----------------Task: 2 shallow copy and deep copy ---------------------------
#===============================================================================


def shallow_copy():
  print("\n---------------- SHALLOW COPY ----------------")
 
  dict_shallow = copy.copy(data)
 
  print("orignal dict: " , data)
  print("Shallow_copy dict: " , dict_shallow)
 
 
  print("Outer ID original: " , id(data))
  print("Outer ID shallow: " , id(dict_shallow))
 
 
  print("Nested shallow:" , id(data['students']))
  print("Nested list ID shallow: " , id(dict_shallow['students']))
  print(" ")
 
 
def Deep_copy():
 
  print("\n---------------- DEEP COPY ----------------")
  dict_deep = copy.deepcopy(data)
  print("orignal dict: " , data)
  print("Deep_copy dict: " , dict_deep)
 
  print("Outer ID original: " , id(data))
  print("Outer ID deep: " , id(dict_deep))
 
 
  print("Nested list ID original: " , id(data['students']))
  print("Nested list ID deep: " , id(dict_deep['students']))
  print("---------------------------------------------------\n")
 
def Append_data():
  data["students"].append("C")
  print("After Appending : ", data)
  print("---------------------------------------------------\n")
 



#====================================================================
#------------------task-3 Python collections------------------------
#====================================================================

   
def Add_Course(c):
  print("\n---------------- ADD COURSE ----------------")  
  courses.append(c)
  print(courses)
  print("------------------------------------------------\n")
 
def Search_By_Id(S_id):
    print("\n---------------- SEARCH STUDENT ----------------")
    if S_id in id_name:
      print("Found", id_name[S_id])    
    else:
        print("ID not found")
    print("------------------------------------------------\n")

        


def Remove_course():
  print("\n---------------- REMOVE COURSE ----------------")
  course = input("enter a course to remove: ")
  if course in courses:
    courses.remove(course)
    print("Removed:", courses)
  else:
    print("Course not found")
print("------------------------------------------------\n")
 
def Set_Operations():
  print("\n---------------- SET OPERATIONS ----------------")
  new_faculty = {"Dr.Gangwar", "Dr.Khan"}
  union_of_sets = faculty.union(new_faculty)
  print("Union operation \n", union_of_sets)
 
  intersection_of_sets = faculty.intersection(new_faculty)
  print("Intersection operation \n", intersection_of_sets)
  print("------------------------------------------------\n")



#====================================================================
#------------------task-4 lamda function-----------------------------
#====================================================================


def sort_by_name():
  print("\n---------------- SORT BY NAME ----------------")

  sorted_list = sorted(students_detail, key= lambda x: x[1])
  print("Sorted by Name:")
  for item in sorted_list:
    print(item)
print("------------------------------------------------\n")
 
def sort_by_id():
  print("\n---------------- SORT BY ID ----------------")
  sorted_list = sorted(students_detail, key= lambda x: x[0])
  print("Sorted by ID:")
  for item in sorted_list:
    print(item)
    
print("------------------------------------------------\n")



#=========================================================================
# ------------------ TASK 5 : File & Exception Handling -----------------
#=========================================================================

 
def write_mode_demo():
    print("\n--------WRITE MODE-----------")
    try:
        with open("sample.txt", "w") as f:
            f.write("Line 1: Python\n")
            f.write("Line 2: File Handling\n")
        print("File written successfully using w mode.")
        
        created_files.add("sample.txt")
        features_ran.add("File write")
        print(" ") 
 
    except OSError as e:
        print("File writing error:", e)
    print("------------------------------------------------\n")    


 
def append_mode_demo():
 
    print("\n---------a MODE-----------")
    try:
        with open("sample.txt", "a") as f:
            f.write("Line 3: Appended Line\n")
        print("Data appended successfully using a mode.")
        print("------------------------------------------------\n")
 
    except OSError as e:
        print("File append error:", e)
 
features_ran.add("File appendded")

 
def read_modes_demo():
 
    print("\n-------------r MODE--------------")
    try:
        with open("sample.txt", "r") as f:
            print("Using read():")
            print(f.read(40))  # small preview
 
        with open("sample.txt", "r") as f:
            print("\nUsing readline():")
            print(f.readline())
 
        with open("sample.txt", "r") as f:
            print("\nUsing readlines():")
            print(f.readlines())
            print("------------------------------------------------\n")

 
    except FileNotFoundError:
        print("File not found. Please write the file first.")
 
    except OSError as e:
        print("File read error:", e)
  
 
def r_plus_demo():
 
    print("\n------------------- r+ MODE-------------------")
    try:
        with open("sample.txt", "r+") as f:
            content = f.read(30)
            print("Initial content preview:", content)
            f.write("Added using r+\n")
        print("Write completed in r+ mode.")
        print("------------------------------------------------\n")

 
    except FileNotFoundError:
        print("File not found for r+ mode.")
 
    except OSError as e:
        print("r+ mode error:", e)
    print(" ") 
 
def a_plus_demo():
 
    print("\n------------- a+ MODE-----------------")
    try:
        with open("sample.txt", "a+") as f:
            f.write("Added using a+\n")
            f.seek(0)
            print("Preview after append:", f.read(40))
 
    except OSError as e:
        print("a+ mode error:", e)
    print("------------------------------------------------\n")

   
def divide_demo():
 
    print("\n---------- DIVISION DEMO----------------")
    try:
        num = int(input("Enter a number: "))
        result = num / 0
        print(result)
        print("------------------------------------------------\n")

 
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        logging.error("ZeroDivisionError ocuured")
 
    except ValueError:
        print("Invalid number entered.")
        logging.error("Invalid input provided.")
   



#====================================================================
# ------------------ TASK 6 : Mutithreading--------------------------
#====================================================================


 
def multithreading_demo():
   print("\n----------------MLTITHREADING----------------")
   global shared_resource
   shared_resource = 0
   threads = []
 
   for i in range(2):    
     t = threading.Thread(target= increment)
     threads.append(t)
     t.start()
   
   for t in threads:
      t.join()
   print("Final value with locks: ", shared_resource)
   features_ran.add("Multithreading")
print("------------------------------------------------\n")
 
def increment():
   global shared_resource
   for _ in range(3):
      with lock:
         shared_resource += 1



#============================================================================
# ------------------ TASK 7 : DSA (stack, queue, linkedkist)-----------------
#=============================================================================



def queue_Implementation():
   print("\n---------------- QUEUE ----------------")
   dq = deque()
 
   num = int(input("How many elements to add? "))
 
   for i in range(num):
      value = input("Enter value: ")
      dq.append(value)
   print("\nQueue after adding:", dq)
 
   #----DEQUEUE---------
   print("\nRemoving elements........")
 
   while dq:
      removed = dq.popleft()
      print("Removed: ", removed)
   print("\nQueue after removing:", dq)
   features_ran.add("Que Implementation")
print("------------------------------------------------\n")
 
 

def stack_Implementation():
   print("\n---------------- STACK ----------------")
   stack = []
   num = int(input("How many elements to push? "))
   for i in range(num):
      value = input("Enter value: ")
      stack.append(value)
   print("\nstack after adding:", stack)
 
   #--------POP-----------
   print("\nPopping elements........")
 
   while stack:
      removed = stack.pop()
      print("Popped:", removed)
   print("\nStack after pop:", stack)
   features_ran.add("stack Implementation")
print("------------------------------------------------\n")


#----LINKEDLIST IMPLEMENTATION-------
 
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
class LinkedList:
   print("\n---------------LINKEDLIST ----------------")
   def __init__(self):
      self.head = None #initially list is empty
 
   def add_node(self, name):
      new_node = Node(name)
     
      #If list is empty
      if self.head is None:
         self.head = new_node
         return
      #If list is not empty traverse to last node
      current = self.head
      while current.next:
         current = current.next
      current.next = new_node #attach a new node
 
      #Display list
   def display(self):
      current = self.head
 
      if current is None:
         print("Linked list is empty")
         return
     
      while current:
         print(current.data, end= " -> ")
         current = current.next
      print("None")
 
      #Search node by name
   def search(self, name):
      current = self.head
 
      while current:
            if current.data == name:
               print(name, "Node found in list")
               return
            current = current.next
      print(name, "Not found in list")
     
def linked_list_demo():
         print("\n-----Linked List Demo-----")
 
         l1 = LinkedList()
         l1.add_node("Aman")
         l1.add_node("Ria")
         l1.add_node("John")
 
         print("List after adding nodes: ")
         l1.display()
         l1.search("Aman") #search existing
         l1.search("Sara") #search non-existing
         features_ran.add("LinkedList Implementation")
print("------------------------------------------------\n")



#====================================================================
#----------Task-8 : TREEs and GRAPH  IMPLEMENTATION------------------
#====================================================================
 

def preorder(tree, node):
   print("\n---------------- PREORDER TRAVERSAL---------------")
   print(node, end=" ")
   for child in tree.get(node, []):
      preorder(tree, child)
 
def tree_demo():
   tree = {
      "College": ["Engineering", "Sciene"],
      "Branch": ["CSE", "AI"],
      "Engineering": [],
      "Sciene": [],
      "CSE":[],
      "AI":[]
   }
   print("Preorder Traversal:")
   preorder(tree, "College")
   print()
   features_ran.add("Tree Implementation")
print("------------------------------------------------\n")

 
#---------Graph Implemenation-------
 
def bfs_shortest_path(graph, start, target):
   print("\n----------------GRAPHS---------------")
   visited = set()
   queue = deque([[start]])
 
   while queue:
      path = queue.popleft()
      node = path[-1]
 
      if node == target:
         return path
     
      if node not in visited:
         visited.add(node)
 
         for neighbor in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            queue.append(new_path)
   return None
 
def graph_demo():
   graph = {
      "A":["B","C"],
      "B":["D"],
      "C":["E"],
      "D":[],
      "E":[]
   }
   path = bfs_shortest_path(graph, "A", "E")
   if path:
      print("Shortest path from A to E: ", " -> ".join(path) )
   else:
      print("No path found")
   features_ran.add("Graphs BFS")
   print("----------------------------------\n")


#====================================================================
#---------Task - 9 : Sorting (Bubble sort)--------------------------
#====================================================================


 
def bubble_sort():
   print("\n----------------BUUBLE SORT----------------")
   arr = [5, 2, 9, 1, 3]
 
   print("Before Sorting: ", arr)
 
   n = len(arr)
 
   for i in range(n):
      for j in range(0, n-i-1):
         if arr[j]> arr[j+1]:
            #swap elements
            arr[j], arr[j+1] = arr[j+1], arr[j]
   print("After Sorting: ", arr)
   print("------------------------------------------------\n")
   features_ran.add("Bubble Sort")
  


#====================================================================
#----------------------Task - 10 : OOPs------------------------------
#====================================================================
 
class Person:
   print("\n----------------OOPS----------------")
   def __init__(self, name):
      self.name = name
   def describe(self):
      print(f"Person Name: {self.name}")
 
class Student(Person):
   def __init__(self, name, course):
      super().__init__(name)
      self.course = course
 
   def describe(self):
      print(f"Student Name: {self.name}, Course: {self.course}")
     
class Faculty(Person):
   def __init__(self, name, subject):
      super().__init__(name)
      self.subject = subject
 
   def describe(self):
      print(f"Faculty Name: {self.name}, Subject: {self.subject}")
 
def oop_demo():
   p1 = Student("Aman", "AI")
   p2 = Faculty("Dr. Gangwar", "Networks")
   p3 = Person("Visitor")
   
   people = [p1, p2, p3]
 
   for person in people:
      person.describe()
   features_ran.add("OOP Polymorphism")
   print("------------------------------------------------\n")


#======================================================================
#---------Task - 11 : Security scripting and Regex---------------------
#=======================================================================


 
def log_filter_demo():
   print("\n-----------LOG FILTER----------------")
 
   logs = [
      "INFO User Sam logged in",
      "FAILED login attempt from 192.168.1.10",
      "WARNING Disk space low",
      "admin accessed confidential file",
      "User Riiia logged out"
   ]
   print("Filtered Logs (FAILED or admin): ")
   for line in logs:
      if "FAILED" in line or "admin" in line:
         print(line)
 
def regex_demo():
   print("\n------b) Regex Demo------")
 
   sample = "contact admin at admin123@gmail.com or call 9897872340 immediately."
 
   #Email pattern
   email_pattern = r"\b[\w.-]+@[\w.-]+\.\w+\b"
 
   #10-digit number pattern
   phone_pattern = r"\b\d{10}\b"
 
   emails = re.findall(email_pattern, sample)
   phones = re.findall(phone_pattern, sample)
   
   print("Email Found: ", emails)
   print("10-digit Numbera=s Found: ", phones)
   features_ran.add("Regex")
   print("------------------------------------------------\n")

#======================================================================   
#----------Task - 12 : Socket programming(Server)----------------------
#====================================================================== 

def echo_server():
   print("\n--------------ECHO SERVER--------------")
   #1. create socket object
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #2. Bind socket to host and port
   server_socket.bind(("127.0.0.1", 5000))
   #3. start listening
   server_socket.listen(1)
   print("server is waiting for connenction.......")
 
   #4.Accept connection from client
   client_socket, address = server_socket.accept()
   print("Connected by", address)
   
   while True:
      #5. Recieve data from client and decode bytes to strng
      data = client_socket.recv(1024).decode()
 
      if not data:
         break #client discoonected
      print("Received from client: ", data)
 
      if data.lower() == "exit":
         print("Exit command received. Closing server.")
         break
      #6. Echo back the same data
 
      client_socket.send(data.encode()) #encode string to bytes
 
   #7. close connection and socket
   client_socket.close()
   server_socket.close()
   
 
   #---------Socket programming (Client)-------------------------  
def echo_client():
   print("\n----ECHO CLIENT-------")
 
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
   #2. connect to server
   client_socket.connect(("127.0.0.1", 5000))
   print("Connected to server........")
 
   while True:
      #3. take input from user
      message = input("Enter a meassage or type 'exit' to quit : ")
 
      #4. send meassge to server
      client_socket.send(message.encode())
 
      if message.lower() == "exit":
         print("Existing client..")
         break
      #5. Recieve echo from server
      data = client_socket.recv(1024).decode()
      print("Echo from server: ", data)
 
   client_socket.close()
  

#==============================================================================
#-----------------Task - 13 : JSON Advanced Fle operation---------------------
#=============================================================================


 
def json_handling():
  print("\n----------------JSON HANDLING----------------")
  
  car = """{
"model": "Civic",
"make": "Honda",
"variants":["Sedan","Coupe"]
}"""
  # convert json to python object(Dict)
  car_dict = json.loads(car)
  print(car_dict)
 
  with open("car.json", 'w') as json_file:    
     json.dump(car_dict, json_file, indent = 4)
  print("JSON data added successfullyy...")
 
  created_files.add("car.json")
  features_ran.add("JSON Handling")
  print("------------------------------------------------\n")
 
 #---------CSV write $ read--------------------
def csv_write():
     print("\n---------------- CSV WRITE----------------")
     f = open('names.csv', 'w')
     with f:
        fnames = ['FirstName','LastName']
        writer = csv.DictWriter(f, fieldnames = fnames)
        writer.writeheader()
        writer.writerow({'FirstName':'Nia', 'LastName': 'Singh'})
        writer.writerow({'FirstName':'Ria', 'LastName': 'Singh'})
     print("Data added succuesfully......")
 
     created_files.add("names.csv")
     features_ran.add("CSV Write")
     print("-------------------------------\n")
 
def csv_read():
     print("\n----------------CSV READ----------------")
     fr = open('names.csv', 'r')
     with fr:
        reader = csv.DictReader(fr)
        for row in reader:
           print(row)
     print("Data added succuesfully......")  
     print("------------------------------\n")
 
 #--------- Custom CSV Dialect--------------------
 
def csv_dialect():
   print("\n----------------CSV DIALECT----------------")
   csv.register_dialect("pipe", delimiter="|", quotechar='"')
   with open("register_dialect.csv", "w", newline="") as fc:
      writer = csv.writer(fc, dialect= "pipe")
      writer.writerow(["P_id", "name", "age"])
      writer.writerow(["1", "Sam", "23"])
      writer.writerow(["2", "Raj", "20"])
   
   with open("register_dialect.csv", "r") as f_read:
      reader = csv.reader(f_read, dialect="pipe")
      for row in reader:
         print(row)
   created_files.add("register_dialect.csv")
   features_ran.add("CSV Dialect")
   print("------------------------------------\n")


#=============================================================================================
#------------------Task - 14 : Advanced: Exceptions & Command-Line Arguments------------------
#=============================================================================================



def calculator_menu():
    import argparse
    print("\n----------------Command-Line Arguments----------------")
    class InvalidOperationError(Exception):
        pass

    def calculate(op, a, b):
        if op == "add":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        else:
            raise InvalidOperationError("Invalid operation selected")

    # Take input from menu
    op = input("Enter operation (add/sub/mul/div): ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    # Convert into argument list like CMD
    argument_list = ["--op", op, "--a", a, "--b", b]

    parser = argparse.ArgumentParser()
    parser.add_argument("--op", required=True)
    parser.add_argument("--a", required=True, type=float)
    parser.add_argument("--b", required=True, type=float)

    try:
        args = parser.parse_args(argument_list)
        result = calculate(args.op, args.a, args.b)
        print("Result:", result)
        print("----------------------------------\n")

    except Exception as e:
        print("Error:", e)
    



#=======================================================================
#--------------Task-15: Logging and debugging---------------------------
#========================================================================


def logging_demo():
    print("\n-------------LOGGING & DEBUGGING -------------------")
    global debug_enabled
 
    level = logging.DEBUG if debug_enabled else logging.INFO
 
    logger = logging.getLogger()
    logger.setLevel(level)
 
    # Remove old handlers (important for toggle)
    if logger.hasHandlers():
        logger.handlers.clear()
 
    file_handler = logging.FileHandler("app.log")
    console_handler = logging.StreamHandler()
 
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
 
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
 
    created_files.add("app.log")
    logging.info("Logging configured. DEBUG=%s", debug_enabled)
 
def toggle_debug():
      global debug_enabled
      debug_enabled = not debug_enabled
      logging_demo()
      print("Debug Mode: ", debug_enabled)
      print("-------------------------------\n")


#====================================================================
#---------------Task-16: Final SUMMARY-------------------------------
#====================================================================
 
def final_summary():
   print("\n--------------FINAL SUMMARY---------------")
   print("Featured Executed: ")
   for f in features_ran:
      print("-", f)
 
   print("\nFiles created: ")
   for file in created_files:
      print("-", file)
      
   print("-----------------------------------\n")

#====================================================================       
#----------------------Menu Driven-----------------------------------
#====================================================================

 
def show_menu():
  print("0. Show Python info: ")
  print("1. shallow_copy: ")
  print("2. Deep_copy: ")
  print("3. Appending data: ")
  print("4. Sorting by name: ")
  print("5. Sorting by ID: ")
  print("6. Add Course: ")
  print("7. Search Student by ID: ")
  print("8. Remove Course: ")
  print("9. Show Set Operations: ")
  print("10. Show w mode: ")
  print("11. Show a mode: ")
  print("12. Show r mode: ")
  print("13. Show r+ mode: ")
  print("14. Show a+ mode: ")
  print("15. show divide_demo: ")
  print("16. show multithreading Implemention ")
  print("17. show Queue Implementaion")
  print("18. show Stack Implementaion")
  print("19. show Linkedlist Implemention")
  print("20. show Tree Implemention")
  print("21. show graph Implemention")
  print("22. Show bubble sort Implemention")
  print("23. show oops Implemenation")
  print("24. Show log filter Implemenation")
  print("25. Show log regex Implemenation")
  print("26. Show server Implemenation")
  print("27. Show clent Implemenation")
  print("28. Show JSON handling Implemenation")
  print("29. Show csv write Operation")
  print("30. Show csv read Operation")
  print("31. Show csv Dialect Implemetation")
  print("32. Toggle DEBUG Logging")
  print("33.Command-Line Arguments")
  print("34. Exit")
  print(" ")
   
logging_demo()
print(" ")
 
while True:
  show_menu()
  try:
      choice = int(input("Enter your choice: "))
  except ValueError:
    print("Enter numbers only")
    continue
 
  if choice == 0:     
     python_info()
  elif choice == 1:
    shallow_copy()    
  elif choice == 2:
    Deep_copy()
  elif choice == 3:
    Append_data()
  elif choice == 4:
    sort_by_name()
  elif choice == 5:
    sort_by_id()
  elif choice == 6:
    c  = input("Enter a course: ")
    Add_Course(c)
  elif choice == 7:
    S_id = int(input("Enter a id: "))
    Search_By_Id(S_id)
  elif choice == 8:
    Remove_course()
  elif choice == 9:
    Set_Operations()
  elif choice == 10:
    write_mode_demo()
  elif choice == 11:
    append_mode_demo()
  elif choice == 12:
    read_modes_demo()
  elif choice == 13:
    r_plus_demo()
  elif choice == 14:
    a_plus_demo()
  elif choice == 15:
    divide_demo()
  elif choice == 16:
    multithreading_demo()
  elif choice == 17:
     queue_Implementation()
  elif choice == 18:
     stack_Implementation()
  elif choice == 19:
     linked_list_demo()
  elif choice == 20:
     tree_demo()
  elif choice == 21:
     graph_demo()
  elif choice == 22:
     bubble_sort()
  elif choice == 23:
     oop_demo()    
  elif choice == 24:
     log_filter_demo()
  elif choice == 25:
     regex_demo()  
  elif choice == 26:
     echo_server()
  elif choice == 27:
     echo_client()
  elif choice == 28:
     json_handling()
  elif choice == 29:
     csv_write()
  elif choice == 30:
     csv_read()
  elif choice == 31:
     csv_dialect()
  elif choice == 32:
     toggle_debug()
  elif choice == 33:
     calculator_menu()
  elif choice == 34:
    logging.info("Application existing-------")
    final_summary()
    print("Exit")
    break
  else:
    print("Invalid choice-- chiiii......")
 
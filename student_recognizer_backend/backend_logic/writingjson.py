import json


	
Student_details = {
	           "Name": "rakesh",
               "Section": "B3",
               "course": "BE CSE - Regular",
               "DOB": "5/03/2002",
               "Block": "1st Block",
               "Email": "rakesh@gmail.com",
               "Mobile Number": "+91 9786374113",
               "Father Name": "ram",
               "Mother Name": "sony",
               "Parents Number": "+91 9723416413",
               "Co-ordinator": "NULL",
               "Boarding Point": "navalur",
               "Acedemic Year": "2021-2025"
 }

value = json.dumps(Student_details, indent=13)

with open("student.json", "w") as outfile:
	 outfile.write(value)
	
   

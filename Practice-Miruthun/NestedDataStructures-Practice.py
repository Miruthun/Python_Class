myData= {
  "Tutor": "Arvinder Pal",
  "Mode": "Online",
  "Bootcamp": "Online Python Course",
  "data": {
    "studentProfile": {
      "personalInfo": {
        "name": "Govind Sharma",
        "age": 12,
        "grade": 7,
        "studentId": "STU123456",
        "dateOfBirth": "2012-04-15",
        "nationality": "Indian",
        "languages": ["English", "Hindi", "Kannada"],
        "contact": {
          "email": "govind.sharma@example.com",
          "phone": "+91-9876543210",
          "address": {
            "street": "123 MG Road",
            "city": "Bangalore",
            "state": "Karnataka",
            "country": "India",
            "pincode": 123456
          },
          "emergencyContact": {
            "name": "Priya Sharma",
            "relationship": "Mother",
            "phone": "+91-9123456789"
          }
        }
      },
      "academicInfo": {
        "course": "Python Programming",
        "enrollmentDate": "2024-09-01",
        "progress": {
          "modulesCompleted": 8,
          "totalModules": 20,
          "percentage": 40.0
        },
        "grades": [
          {"module": "Basics", "score": 85},
          {"module": "Functions", "score": 78},
          {"module": "Data Structures", "score": 92}
        ],
        "attendance": {
          "totalClasses": 50,
          "classesAttended": 48,
          "attendancePercentage": 96.0
        }
      },
      "hobbies": ["Cricket", "Video Games", "Coding", "Music", "Chess"],
      "extracurricular": [
        {
          "activity": "Cricket Club",
          "role": "Member",
          "achievements": ["Best Batsman 2024"],
          "activeSince": "2023-06-01"
        },
        {
          "activity": "Coding Club",
          "role": "Junior Developer",
          "achievements": ["Hackathon Winner 2024"],
          "activeSince": "2024-01-15"
        },
        {
          "activity": "Music Club",
          "role": "Vocalist",
          "achievements": [],
          "activeSince": "2024-10-01"
        }
      ]
    },
    "schoolInfo": {
      "name": "Bright Future Academy",
      "type": "Private International School",
      "established": "2005",
      "accreditation": "CBSE",
      "location": {
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "pincode": 123456,
        "coordinates": {
          "latitude": 12.9716,
          "longitude": 77.5946
        }
      },
      "contact": {
        "email": "contact@bfa.edu.in",
        "phone": "+91-8001234567",
        "website": "https://www.bfa.edu.in"
      },
      "facilities": ["Science Labs", "Library", "Sports Complex", "Computer Labs"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Diverse festivals like Diwali and Holi", "Rich history in mathematics and science"]
    },
    "metadata": {
      "lastUpdated": "2025-06-07T15:30:00Z",
      "source": "Student Management System"
    }
  }
}
# 1)
print("The tutor's name is ", myData["Tutor"], "and the bootcamp is ",myData["Bootcamp"], ".", )

# 2)
print("The student's name is ", myData["data"]["studentProfile"]["personalInfo"]["name"])
print("The student's age is ", myData["data"]["studentProfile"]["personalInfo"]["age"])
print("The student's email is ", myData["data"]["studentProfile"]["personalInfo"]["contact"]["email"])

# 3)
print("He has ", len(myData["data"]["studentProfile"]["hobbies"]), "hobbies")

# 4)
myData["data"]["studentProfile"]["hobbies"].append("Photography")
print("Updated Hobbies: ", myData["data"]["studentProfile"]["hobbies"])

# 5)
myData["data"]["studentProfile"]["hobbies"].remove("Video Games")
print("Updated Hobbies without Video Games: ", myData["data"]["studentProfile"]["hobbies"])

# 6)
print("Student's school name is ", myData["data"]["schoolInfo"]["name"])
print("Student's school facilities are ", myData["data"]["schoolInfo"]["facilities"])

# 7)
if myData["data"]["countryInfo"]["timezone"] == "IST (UTC+5:30)":
    print("Yes, timezone is IST, which is UTC + 5:30")
else:
    print("No, timezones are not matching")

# 8)
print("The nationality of the student is", myData["data"]["studentProfile"]["personalInfo"]["nationality"])

# 9)
print("The languages that the student can speak are", myData["data"]["studentProfile"]["personalInfo"]["languages"])

# 10) 
print("The student's school contact email is ", myData["data"]["schoolInfo"]["contact"]["email"])

# 11) 
if myData["data"]["schoolInfo"]["accreditation"] == "CBSE":
    print("Yes, the school's accreditation is CBSE.")
else:
    print("No, the school's accreditation is not CBSE")

# 12)
for item in myData["data"]["studentProfile"]["academicInfo"]["grades"]:
    if item["score"]>85:
        print("The module that the student got a grade of above 85 is ", item)
    else:
        continue

# 13)
myData["data"]["studentProfile"]["academicInfo"]["grades"].append({"module":"Algorithms", "score": 87})
print("This is the new grades: ", myData["data"]["studentProfile"]["academicInfo"]["grades"])

# 14)
y=0
z=0
for item in myData["data"]["studentProfile"]["academicInfo"]["grades"]:
    y+=item["score"]
    z+=1
print("The average score is ", y/z)

# 15)
print("The student's address is ", myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]["street"], myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]["city"], ",", myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]["state"], ",", myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]["country"])

# 16)
del myData["data"]["schoolInfo"]["location"]["coordinates"]
print("The new location info is ", myData["data"]["schoolInfo"]["location"])

# 17)
myData["data"]["studentProfile"]["personalInfo"].update(age = 13)
print("The updated age is ", myData["data"]["studentProfile"]["personalInfo"]["age"])

# 18)
for item in myData["data"]["studentProfile"]["extracurricular"]:
    print(item["activity"], ": ", item["role"])

# 19)
a = myData["data"]["studentProfile"]["academicInfo"]["attendance"]["totalClasses"] - myData["data"]["studentProfile"]["academicInfo"]["attendance"]["classesAttended"] 
print("The student missed", a, "classes")

# 20)
print("The student's country's cultural highlights are ", myData["data"]["countryInfo"]["culturalHighlights"])

# 21)
if myData["data"]["studentProfile"]["personalInfo"]["contact"]["address"]["pincode"] == myData["data"]["schoolInfo"]["location"]["pincode"]:
    print("Yes, the pincode matches")
else:
    print("No, the pincodes do not match")

# 22)
myData["data"]["studentProfile"]["extracurricular"].append("{'activity': 'Debate Club', " \
"'role' : 'speaker', " \
"'achievements': []," \
"'activeSince' : '2025-02-01'}")
print()
print("Updated Extracurriculars: ", myData["data"]["studentProfile"]["extracurricular"])

# 23) 
item = myData["data"]["studentProfile"]["extracurricular"]
counter=0

for i in range(len(item)):
    if len(item[i]["achievements"][0]) > 0:
        counter+=1
print(counter)

'''
totalAchievements = len(item["achievements"])
print(totalAchievements)
'''
print(len(item[0]["achievements"]))
print(len(item))
print(item[0]["achievements"][0])
# 24)
'''
mostRecentactivity = myData["data"]["studentProfile"]["extracurricular"][0]
latestDate = myData["data"]["studentProfile"]["extracurricular"][0]["activeSince"]
for activity in myData["data"]["studentProfile"]["extracurricular"][1:]:
    currentDate = activity["activeSince"]
    print(currentDate)
'''

# 25)
# Told to Skip
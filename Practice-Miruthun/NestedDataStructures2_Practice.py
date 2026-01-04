mydata= [
  {
    "studentProfile": {
      "personalInfo": {
        "name": "Ananya Patel",
        "age": 13,
        "grade": 8,
        "studentId": "STU789012",
        "dateOfBirth": "2012-07-22",
        "nationality": "Indian",
        "languages": ["English", "Gujarati", "Hindi"],
        "contact": {
          "email": "ananya.patel@example.com",
          "phone": "+91-8765432109",
          "address": {
            "street": "45 Sardar Road",
            "city": "Ahmedabad",
            "state": "Gujarat",
            "country": "India",
            "pincode": 380001
          },
          "emergencyContact": {
            "name": "Ravi Patel",
            "relationship": "Father",
            "phone": "+91-9012345678"
          }
        }
      },
      "academicInfo": {
        "course": "Web Development",
        "enrollmentDate": "2024-08-15",
        "progress": {
          "modulesCompleted": 10,
          "totalModules": 25,
          "percentage": 40.0
        },
        "grades": [
          {"module": "HTML", "score": 88},
          {"module": "CSS", "score": 82},
          {"module": "JavaScript", "score": 90}
        ],
        "attendance": {
          "totalClasses": 60,
          "classesAttended": 57,
          "attendancePercentage": 95.0
        }
      },
      "hobbies": ["Painting", "Dance", "Coding", "Reading"],
      "extracurricular": [
        {
          "activity": "Dance Club",
          "role": "Choreographer",
          "achievements": ["First Place in State Competition 2024"],
          "activeSince": "2023-09-10"
        },
        {
          "activity": "Art Club",
          "role": "Member",
          "achievements": [],
          "activeSince": "2024-02-20"
        }
      ]
    },
    "schoolInfo": {
      "name": "Sunrise International School",
      "type": "Private",
      "established": "2010",
      "accreditation": "CBSE",
      "location": {
        "city": "Ahmedabad",
        "state": "Gujarat",
        "country": "India",
        "pincode": 380001,
        "coordinates": {
          "latitude": 23.0225,
          "longitude": 72.5714
        }
      },
      "contact": {
        "email": "info@sunrise.edu.in",
        "phone": "+91-7923456789",
        "website": "https://www.sunrise.edu.in"
      },
      "facilities": ["Art Studio", "Dance Hall", "Computer Labs", "Library"]
    },
    "countryInfo": {
      "name": "India",
      "capital": "New Delhi",
      "officialLanguage": ["Hindi", "English"],
      "currency": "Indian Rupee (INR)",
      "timezone": "IST (UTC+5:30)",
      "culturalHighlights": ["Vibrant textile traditions", "Gujarati folk dance Garba"]
    }
  },
  {
    "studentProfile": {
      "personalInfo": {
        "name": "Liam Chen",
        "age": 14,
        "grade": 9,
        "studentId": "STU345678",
        "dateOfBirth": "2011-03-10",
        "nationality": "Singaporean",
        "languages": ["English", "Mandarin", "Malay"],
        "contact": {
          "email": "liam.chen@example.com",
          "phone": "+65-91234567",
          "address": {
            "street": "12 Orchard Lane",
            "city": "Singapore",
            "state": "",
            "country": "Singapore",
            "pincode": 238863
          },
          "emergencyContact": {
            "name": "Mei Chen",
            "relationship": "Mother",
            "phone": "+65-98765432"
          }
        }
      },
      "academicInfo": {
        "course": "Robotics",
        "enrollmentDate": "2024-07-01",
        "progress": {
          "modulesCompleted": 12,
          "totalModules": 30,
          "percentage": 40.0
        },
        "grades": [
          {"module": "Mechanics", "score": 85},
          {"module": "Programming", "score": 92},
          {"module": "Sensors", "score": 78}
        ],
        "attendance": {
          "totalClasses": 45,
          "classesAttended": 44,
          "attendancePercentage": 97.8
        }
      },
      "hobbies": ["Robotics", "Chess", "Swimming", "Music"],
      "extracurricular": [
        {
          "activity": "Robotics Club",
          "role": "Team Lead",
          "achievements": ["National Robotics Champion 2024"],
          "activeSince": "2023-05-15"
        },
        {
          "activity": "Chess Club",
          "role": "Member",
          "achievements": ["School Tournament Runner-Up 2024"],
          "activeSince": "2024-01-10"
        }
      ]
    },
    "schoolInfo": {
      "name": "Global Academy Singapore",
      "type": "International",
      "established": "2008",
      "accreditation": "IB",
      "location": {
        "city": "Singapore",
        "state": "",
        "country": "Singapore",
        "pincode": 238863,
        "coordinates": {
          "latitude": 1.3521,
          "longitude": 103.8198
        }
      },
      "contact": {
        "email": "contact@globalacademy.sg",
        "phone": "+65-67891234",
        "website": "https://www.globalacademy.sg"
      },
      "facilities": ["Robotics Lab", "Swimming Pool", "Library", "Auditorium"]
    },
    "countryInfo": {
      "name": "Singapore",
      "capital": "Singapore",
      "officialLanguage": ["English", "Mandarin", "Malay", "Tamil"],
      "currency": "Singapore Dollar (SGD)",
      "timezone": "SGT (UTC+8:00)",
      "culturalHighlights": ["Multicultural festivals", "Advanced technology hub"]
    }
  }
]



# 1)
print("The first student's name and ID is", mydata[0]["studentProfile"]["personalInfo"]["name"], ",", mydata[0]["studentProfile"]["personalInfo"]["studentId"])

# 2)
print("The second student has", len(mydata[1]["studentProfile"]["hobbies"]), "hobbies")

# 3)
mydata[0]["studentProfile"]["hobbies"].append("Photography")
print("The first students updated hobbies are", mydata[0]["studentProfile"]["hobbies"])

# 4)
mydata[1]["studentProfile"]["hobbies"].remove("Swimming")
print("The second students updated hobbies are", mydata[1]["studentProfile"]["hobbies"])

# 5)
print("The first student's school name and website are", mydata[0]["schoolInfo"]["name"], ",", mydata[0]["schoolInfo"]["contact"]["website"])

# 6)
if mydata[0]["countryInfo"]["timezone"] == "IST (UTC+5:30)":
    print("Yes, the student's timezone is IST")
else:
    print("No, the timezones are not matching")

# 7)
print("The nationality of the second student is", mydata[1]["studentProfile"]["personalInfo"]["nationality"])

# 8)
print("The first student can speak", mydata[0]["studentProfile"]["personalInfo"]["languages"])

# 9)
print("The second student's school's email is", mydata[1]["schoolInfo"]["contact"]["email"])

# 10)
if mydata[1]["schoolInfo"]["accreditation"] == "IB":
    print("Yes, the second student's school's accreditation is IB")
else:
    print("No, the school isn't IB")

# 11)
trueProgress = (mydata[0]["studentProfile"]["academicInfo"]["progress"]["modulesCompleted"]/mydata[0]["studentProfile"]["academicInfo"]["progress"]["totalModules"])*100
mydata[0]["studentProfile"]["academicInfo"]["progress"]["percentage"] = trueProgress
print("The updated progress percentage is", mydata[0]["studentProfile"]["academicInfo"]["progress"]["percentage"])

# 12)
print("These are the modules that the second student got more than 85 on:")
for item in mydata[1]["studentProfile"]["academicInfo"]["grades"]:
    if item["score"]>85:
        print(item["module"])
print()

# 13)
newModuleDict = {"module": "Python", "score": 89}
mydata[0]["studentProfile"]["academicInfo"]["grades"].append({"module": "Python", "score": 89})
print("The new grades are",mydata[0]["studentProfile"]["academicInfo"]["grades"] )

# 14)
totalScore = 0
gradeNum = 0
for item in mydata[0]["studentProfile"]["academicInfo"]["grades"]:
    totalScore += item["score"]
    gradeNum +=1
print("The second student's average score is", totalScore/gradeNum)

# 15)
print("The first student's address is", mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["street"], mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["city"], mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["state"], mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["country"])

# 16)
del mydata[0]["schoolInfo"]["location"]["coordinates"]
print("Updated location of first student's school", mydata[0]["schoolInfo"]["location"])

# 17)
mydata[0]["studentProfile"]["personalInfo"]["age"] = 15
print("The second student's updated age is", mydata[0]["studentProfile"]["personalInfo"]["age"])

# 18)
for item in mydata[0]["studentProfile"]["extracurricular"]:
    print(item["activity"], ":", item["role"])

# 19)
totalClasses = mydata[1]["studentProfile"]["academicInfo"]["attendance"]["totalClasses"]
classesAttended = mydata[1]["studentProfile"]["academicInfo"]["attendance"]["classesAttended"]
classesMissed = totalClasses-classesAttended
print("The first student missed", classesMissed, " class(es)")

# 20)
print("The second student's country, Singapore, has these cultural highlights: ", mydata[1]["countryInfo"]["culturalHighlights"])

# 21)
if mydata[0]["studentProfile"]["personalInfo"]["contact"]["address"]["pincode"] == mydata[0]["schoolInfo"]["location"]["pincode"]:
    print("Yes, the first student's pincodes both match")
else:
    print("no, the pincodes do not match")

# 22)

mydata[1]["studentProfile"]["extracurricular"].append({'activity': 'Debate Club', " \
"'role' : 'speaker', " \
"'achievements': []," \
"'activeSince' : '2025-03-01'})
print()
print("Updated Extracurriculars: ", mydata[1]["studentProfile"]["extracurricular"])

# 23)
# Told to Skip

# 24)
student1Att_Percent = mydata[0]["studentProfile"]["academicInfo"]["attendance"]["attendancePercentage"]
student2Att_percent = mydata[1]["studentProfile"]["academicInfo"]["attendance"]["attendancePercentage"]
if student1Att_Percent > student2Att_percent:
    print("Student 1 has the higher attendance percentage at", student1Att_Percent, "%")
elif student2Att_percent > student1Att_Percent:
    print("Student 2 has the higher attendance percentage at", student2Att_percent, "%")

# 25)
# Told to Skip
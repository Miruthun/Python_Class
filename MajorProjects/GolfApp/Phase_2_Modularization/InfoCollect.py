# My Employee Info Collection Function
def infoCollect():
    while True:
        Name = str(input("Please Enter Your Name: ")).strip()
        if not Name:
            print("Empty Name Field. Please Enter Valid Name.")
            continue
        else:
            break
    while True:
        EID = str(input("Please Enter Your Employee ID: ")).strip()
        if not EID:
            print("Empty EID Field. Please Enter Valid EID.")
            continue
        else:
            break
    return {
        "Employee Name": Name,
        "Employee ID": EID
    }
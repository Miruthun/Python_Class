# My Validation Functions
def int_check(Question: str, minNum: int, maxNum: int):
    while True:
        try:
            intResponse = int(input(f'{Question} - between {minNum} & {maxNum}: '))
            if intResponse > maxNum or intResponse < minNum:
                print(f"Sorry, but the number you have entered is out of bonds. Please try again, within {minNum} - {maxNum}")
                continue
            else:
                return intResponse
        except ValueError:
            print("ERROR! PLEASE ENTER NUMERICAL VALUES ONLY!")

def name_check(Question: str, Data):
    while True:
        Inputed = input(Question)
        if Inputed in Data:
            return Inputed
        else: 
            print("ERROR: What you have entered is invalid. Please try again.")
            continue
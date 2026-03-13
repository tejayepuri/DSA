
def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end="")
        print()
star_pattern(5)

def star_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(" * ", end="")
        print()
star_pattern(5)


def number_pattern(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()
number_pattern(5)        


student_name=""
student_status=""

def show_menu():
    print("\n----attendence tracker----")
    print("1. add attendence")
    print("1. view attendence")
    print("3. exit")

def add_attendence():
    global student_name
    global student_status
    print("attendence added successfully")

def view_attendence():
    if student_name="":
        print("no attendence record found")

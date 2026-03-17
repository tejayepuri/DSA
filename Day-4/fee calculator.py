def calculate_fee(course,marks):
    
    if course=="AI":
        fee= 50000
    elif course=="Web":
        fee= 30000
    elif course=="Data Science":
        fee= 40000
    else:
        return None #invalid course


#discount condition
    if marks >90:
        fee -= 5000
    return fee


def main():
    course=input("enter the course:")
    marks=int(input("enter the marks:"))
    fee = calculate_fee(course,marks)

    if fee is None:
        print("Invalid course selected")
    else:
        print("Final fee:", fee)

main()        
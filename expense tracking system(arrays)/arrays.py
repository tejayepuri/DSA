
'''
def count_sum(arr):
    total=0
    for num in arr:
        total +=num
    return total
arr=[1,2,3,4,5]
print('sum', count_sum(arr))


#counting the digits in array

def count_len(array):
    for num in arr:
        return len(arr)
arr=[1,2,3,4,5]
print('count', count_len(arr))



#no of even in the array

def count_even(arr):
    count=0
    for n in arr:
        if n%2==0:
            print(n)
            count+=1
        else:
            continue
    return count    
arr=[1,2,3,4,5,6,7,8]
print('count',count_even(arr))


#biggest number in an array

def max_count(arr):
    count=0
    for i in arr:
        if i > max:
            max_value=1
        return max_value
arr=[2,4,6,98]
print('count',max_count(arr))
'''


#file handling expense tracking system

expenses=[]

def export_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense['name']+ " " +expense["amount"] + "\n")
def main():
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Export expenses")
        print("4.Exit")

        choice=input("enter your choice:")
        if choice =="1":
            name=input("enter expense name:")
            amount=input("enter expense amount:")

            expenses.append({'name':name,'amount':amount})
        elif choice== '2':
            for expense in expenses:
                print(expense["name"]+ "-",expense['amount'])

        elif choice== '3':
            export_expenses(expenses)
        elif choice =='4':
            print("Exiting the program")
            break
        else:
            print("Invalid Choice. Try Again")
main()            


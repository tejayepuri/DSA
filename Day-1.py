def calculate_sum(n):
    total=0
    for i in range(1,n+1):
        total +=i
    return total
def main():
    n=6
    print("sum",calculate_sum(n))
main()

def even_nos(n):
    count= 0
    for i in range(1,n+1):
        if i % 2 == 0:
            print(i)
            count+=1
    return count
def main():
    n=7
    print("even numbers:", even_nos(n))
main()    

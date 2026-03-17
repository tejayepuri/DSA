'''
def count_chars(text):
    count=0
    for char in text:
        count+=1
    return count
def main():
    text=input("enter name:")
    print("characters count:",count_chars(text))
main()
'''

'''
def count_vowels(text):
    count=0
    vowels='a,e,i,o,u,A,E,I,O,U'
    for char in text:
        if char in vowels:
            count+=1
    return count
def main():
    text=input("enter name:")
    print("vowels count:",count_vowels(text))
main()

'''
###reversing a text


def rev_text(text):
    reversed_text=""
    for char in text:
        reversed_text=char+reversed_text
    return reversed_text
text=input("enter text:")
print("reversed_text:",rev_text(text))

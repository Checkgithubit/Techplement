
import random

password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
           '0','1','2','3','4','5','6','7','8','9','#','@','!','%','$','+','*','(' ,')','&','?']

#print list
print(password)
print("Hello guys Welcome to password generator")
p_passing=int(input("Enter password length\n"))

posting=""
for i in range(1,p_passing+1):
    s1=random.choice(password)
#concatenate
    posting=posting+s1

print("Your password is:",posting)

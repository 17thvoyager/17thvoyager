# UPPER CASE ONLY

# from random import randint
# a=""
# for i in range(10):
#     i=chr(randint(65,90))
#     a=str(a)+i
# print(a)


# UPPER AND LOWER CSES AND ALSO INTEGERS
from random import randint
password=""
for i in range(5):
    i=chr(randint(65,90))
    for j in range(5):
        j=chr(randint(65,90)).lower()
        for k in range(5):
            k=chr(randint(48,57))         #----------------> i dont know the purpose of str()
    password=str(password)+i+j+k
print(password)








import string
import random
flag='this is fake flag'
ciphertext=''
alphabet=[]
flag_array=[]
check=[]
key=[]
for i in range(97,123):
    alphabet.append(chr(i))
    key.append(chr(i))

for i in range(len(flag)):
    flag_array.append(flag[i])
    check.append(1)

random.shuffle(key)
key_string=""
for i in key:
    key_string+=i

print(key_string)
for i in range(len(alphabet)):
    for j in range(len(flag)):
        if check[j]:
            if alphabet[i]==flag_array[j]:
                check[j]=0
                flag_array[j]=key[i]
for i in flag_array:
    ciphertext+=i
print(ciphertext)


print(random.random())
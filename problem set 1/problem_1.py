s
count=0
vowels=['a','e','i','o','u']
for i in s:
    if i in vowels:
      count+=1
    else:
      continue

print("Number of vowels: ",count)

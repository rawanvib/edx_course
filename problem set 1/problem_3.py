# Paste your code into this box 
s
res = ''
tmp = ''

for i in range(len(s)):
    tmp += s[i]
    if len(tmp) > len(res):
        res = tmp
    if i > len(s)-2:
        break
    if s[i] > s[i+1]:
        tmp = ''

print("Longest substring in alphabetical order is: {}".format(res))

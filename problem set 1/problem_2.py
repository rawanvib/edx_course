# Paste your code into this box 
s
count=0
for i in range(len(s)-2):
    if s[i:i+3]=='bob':
        count+=1
    else:
        continue
        
print("Number of times bob occures is: ",count)

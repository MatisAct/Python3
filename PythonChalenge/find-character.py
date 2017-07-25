import re
dich=open ('alphabet.txt','r').read()
print ("".join(re.findall(r"\d", dich))) # tìm các kí tự là số trong file
print ("".join(re.findall("[A-Za-z]", dich))) #tìm kí tự là string trong file 

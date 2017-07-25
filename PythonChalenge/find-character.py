import re
dich=open ('alphabet.txt','r').read()
print ("".join(re.findall(r"\d", dich))) # tìm các kí tự là số trong file
print ("".join(re.findall("[A-Za-z]", dich))) #tìm kí tự là string trong file 	
print ("".join(re.findall(r"[A-Za-z]{9,16}", dich))) #tìm kí tự dài từ 9-16,\w kí tự bất kì cặp số {số kí tự ít nhất, kết thúc}
print ("".join(re.findall(r"[A-Z]\w{1,}\s", dich))) #tìm kí tự là string trong file bắt đầu bằng từ in hoa,\s là kết thúc = space

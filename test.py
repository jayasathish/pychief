import requests
import re
a=requests.get("https://imgctcf.aeplcdn.com/thumbs/p-nc-a-ver5/images/car-data/big/hyundai-elantra-default.jpg")
cont=a.content
file=open("test.jpg","wb")
file.write(cont)
file.close()
# file=open("test.html","r")
# r_cont=file.read()
# href=re.findall("href=\"([^>]*?)\"",str(r_cont))
# for i in re.findall("href=\"([^>]*?)\"",str(r_cont)):
    # print(i)


    # file=open("test.txt","w")
    # file.write(str(1))
# file.close()


# for i in range(1,5):
    # file=open("test.txt","a")
    # file.write(str(i)+"\n")
    # file.close()
    
    
# file=open("test.txt","r")
# sat=file.readline() 
# for i in sat:
    # print(i)
# sat=file.readline() 
# sat=file.readlines() 

# file.close()


# import re 
# a="1234dfasknkja143457NVXNV29E03420RMHJWDX83949"
# for res in re.findall("(\d+)",a):
    # print(res)\W\w*?
    
    
    
 
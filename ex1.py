soat = input("Sana kiriting : ")
oy = {1 : "yanvar" , 2 : "fevral" , 3 : "mart" , 4 : "aprel" , 5 : "may" , 6 : "iyun" , 7 : "iyul" , 8 : "avgust" , 9 : "sentabr" , 10 : "oktabr" , 11 : "noyabr" , 12 : "dekabr"}
li = soat.split(" ")
sana = li[0].split(".")
soatt = li[-1].split(".")
oyy = sana[1]
for i in  oy.keys(): 
    g = " "
    if "0" in sana[0]:
        g += sana[0][-1]
    else:
        g += sana[0]
    if str(i) in sana[1]:
        g += "-" + oy[i]
        break
print(sana[-1] , "yil" , g , soatt[0] , "soat" , soatt[1] , "daqiqa")
    



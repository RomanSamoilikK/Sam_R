# 7.	Найти самое длинное слово в строке.
string = ('Depeche Mode violator songsdict ')
b= string.split()
c= sorted(b,key=len)
print(c[-1])

d1=int(input("d1"))
d2=int(input("d2"))
d3=int(input("d3"))
d4=int(input("d4"))
d5=int(input("d5"))
d6=int(input("d6"))
d7=int(input("d7"))
d8=int(input("d8"))
d9=int(input("d9"))
ld=((d1*10+d2*9+d3*8+d4*7+d5*6+d6*5+d7*4+d8*3+d9*2)%11)

if ld==10:
    print("X")
else:
    print("no")
    

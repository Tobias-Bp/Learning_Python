

def division_entera(divisor,dividendo):
	return(divisor//dividendo,divisor%dividendo)

p = int(input("Divisor"))
q = int(input("Dividendo"))

(c,r) = division_entera(p,q)

print("Cociente:",c,"\tResto:",r)
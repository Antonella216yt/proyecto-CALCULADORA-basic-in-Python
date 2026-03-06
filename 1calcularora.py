pedir1=int (input('dame numero 1;'))
pedir2=int (input('dame numero 2;'))
a= input ("ingrese la operacion ")
if a =="+":
    sumar  = pedir1 + pedir2 
    print ("el resultado es",sumar) 


elif a == "-":
    restar= pedir1-pedir2
    print("el resultado es",restar)


elif a == "*": 
    multiplicar= pedir1*pedir2
    print("el resultado es",multiplicar)

elif a =="/":
    division = pedir1/pedir2
    print("el resultado es",division)

elif a== "%":
    modulo = pedir1%pedir2
    print("el resultado es",modulo)


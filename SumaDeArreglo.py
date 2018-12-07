__author__ = 'sugeidy mejia popoca'

def SumaNumeroEntero(numero):
    if len(numero)==1:
        return numero[0]
    else:
        return numero[0] + SumaNumeroEntero(numero[1:])
print(SumaNumeroEntero([3,5,8,10,15,25]))

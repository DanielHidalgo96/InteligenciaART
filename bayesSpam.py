import json
import re
with open('Spam.json') as file:
	data = json.load(file)
Total=0
muestra = 0
L1=[]
Puntuaciones=[]
##Se saca el total del espacio muestral
for Spam in data['Probabilidad']:
	Total=Total+Spam['Total']
	L1.append(Spam['Token'])
"""Se hace una compresion de listas para poder generara la matriz con las probabilidades calculadas"""
L=[e for e in data['Probabilidad']]
MatProb=[]
"""Se crea la matriz con las probabilidades ya calculadas"""
for i in range(len(L1)):
	D=next(item for item in L if item['Token']==L1[i])
	MatProb.append({'Token':D['Token'],'ProbSpam':D['Spam'],'ProbNoSpam':D['NoSpam'],'Total':D['Total']})
MSG="""Increible ganaste un Iphone 10 solo envia
tus datos al siguinete enlace y sera tuyo"""
x=MSG.split()
for e in MatProb:
	R=re.search(
		e['Token'],MSG, flags=re.IGNORECASE)
	if R:
		print("Encontrado",e['Token'])
		Puntuaciones.append((e['ProbSpam'],e['ProbNoSpam'],e['Total'],e['Token']))
print(Puntuaciones)
TotPro=Puntuaciones[0][2]+Puntuaciones[1][2]
print("BAYES INGENUO")
CalcSpam=((Puntuaciones[0][0]/TotPro)*(Puntuaciones[1][0]/TotPro))*TotPro
CalcNSpam=((Puntuaciones[0][1]/Total)*(Puntuaciones[1][1]/Total))*Total
print(CalcSpam/(CalcSpam+CalcNSpam)*100)
print("BAYES probabilidad de que un correo sea Spam si contiene la palabra Increible o Ganaste")
print(Puntuaciones)
b=Total-TotPro
CalcBay=(Puntuaciones[0][0]/TotPro)*(TotPro/Total)
CalcBay2=((Puntuaciones[0][0]/TotPro)*(TotPro/Total))+((Puntuaciones[0][1])/b)*(b/Total)
SP=(CalcBay/CalcBay2)*100
print(round(SP,3))
if round(SP) in range(60, 100): # si n está en el rango 60 - 100*
    print("El correo es Spam")
else:
    print("El correo es HAM")
Calc=(Puntuaciones[1][0]/TotPro)*(TotPro/Total)
Cal=((Puntuaciones[1][0]/TotPro)*(TotPro/Total))+((Puntuaciones[1][1])/b)*(b/Total)
SP1=(Calc/Cal)*100
print(round(SP1,3))
if round(SP1) in range(60, 100): # si n está en el rango 60 - 100*
    print("El correo es Spam")
else:
    print("El correo es HAM")

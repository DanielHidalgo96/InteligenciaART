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
	MatProb.append({'Token':D['Token'],'ProbSpam':D['Spam']/Total,'ProbNoSpam':D['NoSpam']/Total,'Total':D['Total']})
MSG="""Felicidades ganaste un Iphone 10 y $200,000 en Dinero electronico solo envia
tus datos al siguinete enlace y sera tuyo"""
x=MSG.split()
for e in MatProb:
	R=re.search(
		e['Token'],MSG, flags=re.IGNORECASE)
	if R:
		print("Encontrado",e['Token'])
		Puntuaciones.append((e['ProbSpam']))
	muestra= muestra+e['Total']
print(Puntuaciones,muestra)

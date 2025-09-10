peso=input('digite o seu peso')
altura=input('digite a sua altura')

imc=peso/altura

if imc<18.5:
    classificacao='abaixo do peso'
elif imc <25:
    classificacao='pesonormal'
elif imc < 30:
    classificacao='sobrepeso'
else:
    classificacao= 'obsidade'
 
     


    
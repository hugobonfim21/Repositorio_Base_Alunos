nome = input("Digite seu nome")
altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso"))

imc=peso/altura*altura

if imc <=18.5:
    print(" voce esta abaixo do peso")
elif imc <=24.9:
    print (nome, "voce esta no peso ideal")
elif imc <=29.9:
    print(nome, 'voce esta acima dp peso ')
elif imc <=34.9:
    print (nome, 'voce esta esta com obsidade grau 1')
elif imc<=39.9:
    print (nome,'voce esta com obsidade grau 2')

else: 
   print (nome, 'voce esta com obsidade grau 3') 

 
#if,elif,else: sao usados para controles e executar para diferenciar tipos de codigos
#float: e usado para usar com numereos e com virgulas
#inpute ultilizado para receber alguma informaçao do terminal

    

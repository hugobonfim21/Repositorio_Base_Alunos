valor=input('digite o valor total da compra')

if valor >= 1000:
     print('desconto = 15',valor*0.15)
elif valor >=500:
     print('desconto = 10',valor*0.10)
elif valor >=100:
     print('desconto = 5',valor*0.05)
else:
     print('desconto = 0',valor*0.0)
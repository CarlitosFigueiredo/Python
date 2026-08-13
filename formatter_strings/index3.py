from datetime import datetime

frutas = ['banana', 'apple', 'mango', 'kiwi']

for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número dde letras: {len(fruta): 3}"
    print(minha_fruta)
    
print()

pi = 3.1415
meu_numero = f"O número PI é: {pi:.1f}"
meu_numero_deslocado = f"O número PI deslocado é: {pi:6.1f}"
meu_numero_preciso = f"O número PI com precisão é: {pi:.4f}"

print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f"A data de hoje é {data}"
minha_data_formatada = f"A data de hoje é {data:%d/%m/%Y}"

print(minha_data)
print(minha_data_formatada)
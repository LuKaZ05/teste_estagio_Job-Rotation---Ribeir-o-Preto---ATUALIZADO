#1) Ao final do processamento, qual será o valor da variável SOMA? o valor da variável SOMA será 91.

#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

numero = int(input("Digite um número: "))

# Inicializa as duas primeiras posições da sequência de Fibonacci
a, b = 0, 1
while b < numero:
    # Calcula o próximo número da sequência de Fibonacci
    a, b = b, a + b

# Verifica se o número informado pertence à sequência de Fibonacci
if b == numero:
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")



#3) Descubra a lógica e complete o próximo elemento:

#a) A lógica é adicionar 2 ao número anterior. Portanto, o próximo elemento é 9.

#b) A lógica é multiplicar o número anterior por 2. Portanto, o próximo elemento é 128.

#c) A lógica é elevar o índice em que o número aparece na sequência ao quadrado. Portanto, o próximo elemento é 49.

#d) A lógica é adicionar 4 ao quadrado do índice em que o número aparece na sequência. Portanto, o próximo elemento é 100.

#e) A lógica é somar os dois números anteriores para obter o próximo número. Portanto, o próximo elemento é 13.

#f) A lógica é somar 2 ao número anterior, exceto pelo sexto elemento que é 20, o qual provavelmente é um erro ou uma exceção na sequência. Portanto, o próximo elemento é 20.


#4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?

'''Para determinar qual veículo estará mais próximo de Ribeirão Preto quando eles se cruzarem na rodovia, precisamos comparar as distâncias que cada veículo percorreu até aquele momento.

O carro sai de Ribeirão Preto em direção a Franca, percorrendo os 100 km de distância a uma velocidade constante de 110 km/h. Supondo que ele não tenha encontrado tráfego intenso, ele levará cerca de 54,5 minutos para percorrer toda a distância (100 km / 110 km/h * 60 minutos/hora).

Já o caminhão sai de Franca em direção a Ribeirão Preto, percorrendo os mesmos 100 km de distância a uma velocidade constante de 80 km/h. No entanto, ele encontrará dois pedágios no caminho, o que atrasará seu progresso. Supondo que cada pedágio leve 5 minutos extras para ser atravessado, o caminhão levará cerca de 77,5 minutos para percorrer toda a distância (100 km / 80 km/h * 60 minutos/hora + 2 * 5 minutos).

Quando os dois veículos se cruzarem na rodovia, terão percorrido juntos a distância total entre as duas cidades, que é de 100 km. No entanto, como o carro tem uma velocidade maior do que o caminhão, ele terá percorrido uma distância maior do que o caminhão até aquele momento.

Para determinar qual veículo estará mais próximo de Ribeirão Preto quando eles se cruzarem, precisamos calcular a distância percorrida por cada um. Como o carro tem uma velocidade constante de 110 km/h e terá levado cerca de 54,5 minutos para chegar ao ponto de encontro, ele terá percorrido uma distância de cerca de 100 km / 60 minutos/hora * 54,5 minutos = 90,9 km.

Já o caminhão tem uma velocidade constante de 80 km/h e terá levado cerca de 77,5 minutos para chegar ao ponto de encontro, percorrendo uma distância de cerca de 100 km / 60 minutos/hora * 77,5 minutos = 129,2 km.

Portanto, quando os dois veículos se cruzarem na rodovia, o carro estará mais próximo de Ribeirão Preto, tendo percorrido cerca de 90,9 km até aquele momento, enquanto o caminhão terá percorrido cerca de 129,2 km.'''




#5) Escreva um programa que inverta os caracteres de um string.

string = input("Digite uma palavra ou frase: ")

inverted = ""
for i in range(len(string)-1, -1, -1):
  inverted += string[i]

print("A string invertida é:", inverted)




def soma ():
        numero1 = float(input("Digite um número"))
        numero2 = float(input("Digite um número"))
        resultado = numero1 + numero2
        print (resultado)
def sub ():  
        numero1 = float(input("Digite um número"))
        numero2 = float(input("Digite um número"))
        resultado = numero1 - numero2
        print("resultado")
def multi ():
        numero1 = float(input("Digite um número"))
        numero2 = float(input("Digite um número"))
        resultado = numero1 * numero2
        print ("resultado")
def div ():   
        numero1 = float(input("Digite um número"))
        numero2 = float(input("Digite um número"))
        resultado = numero1 / numero2
        print("resultado")
def sair ():
        print ("saindo do sistema...")
def pares ():
      quantidade = int(input("Digite quantos dos números pares você precisa"))
      contador = 0
      numero = 1
      while contador < quantidade:
            if numero % 2 == 0:
                  print(f"esses são os números: {numero}")
                  contador += 1
            numero += 1

def ímpares ():
      quantidade = int(input("Digite quantos dos números ímpares você precisa"))
      contador = 0
      numero = 1
      while contador < quantidade:
            if numero % 2 != 0:
                  print(f"esses são os números: {numero}")
                  contador += 1
            numero += 1

def somat ():
    limite = int(input("Digite o limite para calcular o somatório: "))
    resultado = sum(range(1, limite + 1))
    print(f"O somatório dos números até {limite} é: {resultado}")

def fat ():
    num = int(input("Digite um número para calcular o fatorial: "))
    if num == 0:
        print("O fatorial de 0 é 1.")
    else:
        resultado = 1
        for i in range(1, num + 1):
            resultado *= i
        print(f"O fatorial de {num} é: {resultado}")


while True:
    print ("CALCULADORA")
    print ("1 - adição")
    print ("2 - subtração")
    print ("3 - multiplicação")
    print ("4 - divisão")
    print ("0 - sair")
    print ("5 - pares")
    print ("6 - ímpares")
    print ("7 - somatório")
    print ("8 - fatorial")


    opcao = input("escolha uma opção: ")

    if opcao == "1":
        soma()
    elif opcao == "2":
        sub()
    elif opcao == "3":
        multi()
    elif opcao == "4":
        div()
    elif opcao == "0":
        sair()
    elif opcao == "5":
          pares()
    elif opcao == "6":
        ímpares()
    elif opcao == "7":
        somat()
    elif opcao == "8":
        fat()         
    else:
        print ("opção inválida, tente novamente!")
    
        

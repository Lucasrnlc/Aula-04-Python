Nome = input("Digite seu nome: ")
Nota1 = float(input("Digite sua nota: "))
Se = input("Tem mais notas?: ")
Soma = Nota1
contador = 1

while Se == "sim":
    Nota1 = float(input("Digite sua nota: "))
    Soma += Nota1
    Media += 1
    Media_total = Soma / Media
    Se = input("Tem mais notas?: ")

if Media_total >= 5:
    situacao = "aprovado"

else:
     situacao = "reprovado"
print (f"{Nome} Media {Media_total} situacao {situacao}")     

    
  



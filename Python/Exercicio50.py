'''
Exercicio 050
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.
'''

pop_a = int(input("Digite o valor inicial da população da cidade A: "))
pop_b = int(input("Digite o valor inicial da população da cidade B: "))
anos = 0

taxa_a= float(input("Digite o valor da taxa de crescimento da população da cidade A: "))
taxa_b= float(input("Digite o valor da taxa de crescimento da população da cidade B: "))

while True:

    if taxa_a<=taxa_b:
        print("Como a cidade A tem menos habitantes e sua taxa de crescimento é menor do que a da cidade B, seu número de habitantes nunca será maior que a da outra cidade.")
        break
    if pop_a>=pop_b:
        print(f"Vai demorar {anos} anos para a população da cidade A ultrapassar a da cidade B")
        break

    else:
        pop_a += pop_a * taxa_a
        pop_b += pop_b * taxa_b
        anos += 1
   

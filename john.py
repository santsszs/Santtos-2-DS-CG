import os 


palavra_secreta = "lucas"

letras_acertadas = ''

numero_de_tentativas =0
while True: 
    letra_digitada=input("digite uma letra: ")
    numero_de_tentativas+=1
    if len (letra_digitada) >1:
        print("digite apenas uma letra!")
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas+=letra_digitada
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada += '*'
    print(f"a palavra é {palavra_formada}")
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Voce ganhou! parabens')
        print(f'a palavra era {palavra_formada}')
        print(f'tentativas {numero_de_tentativas}')
              

            
            

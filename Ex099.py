#Função 'maior()' recebendo vários parametros.
#Analisar os valores e mostrar o maior de todos e a lista toda com contagem de valores
from time import sleep
def maior(* num):
    print(f'Foram informados {len(num)} valores ao todo. São eles:') #contagem de valores na lista
    for a in num:
        print(a, end=' ', flush=True)  #listagem de todos os valores da lista
        sleep(0.4)
    print()
    sleep(0.4)
    print(f'O maior valor informado foi o {max(num)}.')  #maior valor na lista

maior(3, 5, 2, 293, 0)
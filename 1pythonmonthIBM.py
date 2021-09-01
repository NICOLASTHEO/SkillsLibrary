print('hello world')
starting=('hi world')
print(starting)
from _typeshed import StrOrBytesPath
from os import O_APPEND, O_NDELAY
from posix import EX_CANTCREAT, O_ACCMODE
from typing import Tuple, ValuesView

# "Tipos de Tuples: str (string) ex.:"disco"; inteiros (int) ex.: 12; float ex.: 1.2"


print('cientista Theo!')
print(24)
print(24**2)
print(5**2)
print('cientista Theo, futuro',1+3)
print('hoje é',25+5, 'de julho' )
print('theo')
total_min=(43+42+56)*2
print(total_min)
print(total_min)
print(total_min)
total_min=2+5+3
print(total_min)
total_min=(2+3+1)*2
print(total_min)
print(total_min)
total_hr=total_min/60
print(total_hr)
print('bora de novo')
total_hr=2+3+1
print(total_hr)
total_min=total_hr*60
print(total_min)
total_min=25+58+75+80
total_hr=total_min/60
print(total_hr)
total_seg=total_min*60
print(total_seg)
#string = sequencia de caracteres entre aspas, aspas simples ou duplas, tanto faz.
#string pode conter palavras, digitos, simbolos, qualquer forma ou formato de sequencia.
string=('michael jackson')
name="Michael Jackson"
#ao colocar um núm. e dois pontos estamos dizendo para considerar apenas os elementos da string dentro dos números indicados.
name[0:4]
name[8:12]
#no segundo dois pontos (:) estamos ordenando q o sistemas só considere determinada sequencia de elementos.
name[::2]
name[0:5:2]
name[0:10:3]
name[2:10:3]
#len-> retorna com o número de elementos dentro da tople (). não funciona com lista [], nem com dicionários
len('Michael Jackson')
name='Michael Jackson'
#podemos concatenar elementos de strings diferentes
print=(name)+"is a singer"
statement = name+'is a singer'
print(statement)
name+' is a singer'
3*name
3*'Michael Jackson '
print(name)
name='Michael Jackson'
print(name)
name + "is a singer"
name= name+" is a singer"
print(name)

type(2)
type(2.0)
float(2)
type(int(2.0))

#Boolean são classes de Elementos (funções no python) que retornarão sempre com UMA de DUAS informações: True ou False 
type(True)
type(False)

x=15+35+8*90/3+(5*3)-1
x

print('AB\nC\nDE')
# \ barra invertida representa uma nova linha seguida de valores, ex.:
print("Michael Jackson \n is a singer")
print("Michael \t Jackson")
print("Michael \\ Jackson")
print(r"Michael \ Jackson")
print ("Michael \ Jackson")


print(name.upper())
name=name.upper()
print(name)
name.replace('MICHAEL', 'Theo')
name.replace('MICHAEL', 'THEO')
name.find('EL')
print(name.lower())
#COMANDO coisa .UPPER deixa tudo (a coisa) em caixa alta, comando LOWER deixa em minúscula
name=name.lower()
print(name)

name.find( 'jack')
name.find('Jack&¨$$#')
#quando houver informação errada ou o resultado for falso, teremos -1
'hello mike'.find('mike')

name="Lizz"
print(name[0:2])
name[8:12:2]
name[1::2]
'1'+'2'
name='abcde'
name.find('b')
str(1+1)

#tuples são valores dentro de parenteses
"disco"=str; 12 = int; 1.2= float # ou seja:
#uma tople pode conter str, int e float nela mesma.
tuple1=("disco",12,1.2)
say_what=('say', 'what', 'you', 'will')

#para acessar os elementos dentro da tople usa-se [] assim acessa-se precisamente o elemento desejado.
#basta atentar-se as virgulas , o primento elemento antes da virgula é repres. pelo nº 0 (zero)
#ex.:
say_what=('say', 'what', 'you', 'will')
say_what[0]# o sistema volta com ... say.
say_what[0:2] 
#Se usarmos números negativos entre as chaves [] o resultado é invertido, sendo o número -1 o último número. ex.:
say_what[-1]# o resultado será ....will

say_what[-1]
tuple2=tuple1+("hard rock",10)
print(tuple2)
tuple2[0:3]
tuple2[::2]
#LEN conta o número de elementos da TUPLE, dentro dos parenteses, do 1 ao...; NÃO CONFUNDIR COM o número de toples dentro das toples, do 0 ao ..., pois aqui trata-se do número total de elementos/TOPLES PRINC. E FILHOTES separadas por VIRGULAS na TOPLE
len((tuple2))
len(('disco',12,1.2,'hard rock',10))

#tuples são imutáveis
ratings=(10,9,6,5,10,8,9,6,2)
ratings1=ratings
ratings[2]
ratings=(2,10,1)
print(ratings1)
#UMA TUPLE PODE TER FILHOTES, OU SEJA, TUPLES DENTRO DE Tuple
#filhote=nestling
nt=(1,2,("pop", 'rock'),(3,4),('disco',(1,2)))
#   0 1        2          3           4        
#quando contamos os nestlings iniciamos do 0
nt[2]
nt[2][1]
nt[3][0],nt[3][1]
nt[0]
nt[1]
nt[4]
nt[4][1]
nt[4][0]
nt[4][1][1]
nt[4][1][0]
nt[4][0][4]
nt[4][0][1:3]

# [] = list, elas ordenam as sequencias. Listas são representadas pelas chaves [], dentro da lista pode ter outras listas.
#uma lista pode conter elementos diversos dentro de si, ela é mutável e conseguimos trabalhar com cada um de seus elementos internos.
#dentro de listas podemos ter string, int, float, listas vazias [], outras listas.
#os elementos dentro de uma lista são contados a partir do 0(zero)
["Michael Jackson",10.1,1982]
list=["Michael Jackson",10.1,1982]
list[2]

list[0][0]
list[0][10]
#Podemos combinar/concatenas listas.
l=['Michael Jackson',10.1,1982]
l1=l+['pop',10]
print(l1)

print(list)
list=['Michael Jackson', 10.1,[1,2],('A',1)]
[1,2,3]+[1,1,1]
l1=['theo']
l2=['nicolas']
l1+l2
print(l1+l2)

#se usar o extend mais parenteses e chave, o item será adicionado ao elemeto da lista. ex.:
l=['Michael Jackson', 10.1,1982]
l.extend(['pop',10])
print(l)
l.extend(['final'])
print(l)

#se usarmos append mais parenteses e chave adicionameos o novo elemento à lista. ex.:

l.append(['pop',10])
print(l)
#agora o cumeprimento da da lista é igual a 2, cumprimento é o nº de elem (listas) em uma lista.
l[5]="final"
print(l)
del(l[5])
print(l)

#podemos tbm separar grupos de palavras (1 str com vários grupos) em grupos de palavras distintos, várias strings
#ex.:
'Theo Nicolas é o pai da Laura'
'Theo Nicolas é o pai da Laura'.split(",")
gr="Theo Nicolas é o pai da Laura"
gr.split()
gr.split(",")
gr.split(',')

a=['hard rock', 10, 1.2]
b=a
a[0]
b[0]
del(a[0])
a.extend(['banana'])
a[0]
b[0]
a[0]=[2]
print(a)
list=['Michael Jackson', 10.1,[1,2],('A',1)]
b[0]


#DICIONÁRIOS
#os dicionários tem chaves{} e valores ,, .

# {} CHAVES são os primeiros elementos. elas são únicas e imutáveis.
# as chaves são seguidas de valores, que podem ser imutávesi, mutáveis, duplicados etc, os Valores são separados por virgulas , ,
#cada elemento de uma chave tbm é separado por vírgulas.

dict={'thriller': 1982, 'black in black':1980, 'the dark side of the moon': 1973, 'the bodyguard': 1992}
del(dict['thriller'])
print(dict)
dict['graduation']='2007'
print(dict)
"the bodyguard" in dict
'thriller' in dict
'graduation' in dict

dict.values()
dict.keys()

# SETS / conjuntos - são tipos de coleções, como se organizados em planilhas.
set1={'pop','rock','soul','hard rock','rock','r&b','rock','disco'}
print(set1)
#os resultados dos sets/conjunts NÃO são duplicados.
#NÃO EXISTEM VALORES DUPLICADOS EM UM CONJUNTO.

album_list=['Michael Jackson', 'thriller','thriller', 1982]
print(album_list)
album_set= set(album_list)
print(album_set)

#Com os SET (ou conjuntos) deve-se ter em mente o diagrama de Venn

type(set([1,2,3]))

a={'thriller','black in black', 'ac/dc'}
print(a)
#PODE-SE ADICIONAR OU REMOVER ELEMENTOS A SETs JÁ EXISTENTES, USA-SE OS COMANDOS .ADDD ('OQUE VOU ADICIONAR') OU .REMOVE ('OQUE VOU REMOVER')
#EX.:
a.add('nysinc')
print(a)
a.remove('nysinc')
print(a)
#PARA CHECAR SE DETERMINADO ELEMENTO ESTÁ EM UM CONJUNTO(SET) USA-SE 'O Q QUER CHECAR' IN NOME DO DIAGRAMA, TEREMOS UM 
#RESULTADO TRUE ou FALSE
'thriller' in a
#o retorno será True

'daiane' in a
#o retorno será False

x=('hd','rv','fv','ro')
'rv' in x
'fo' in x
x=set(x)
print(x)
x.add('fo')
x.remove('hd')
print(x)
x=list(x)
x=set(x)
x.add('hd')
print(x)

#DIAGRAMA DE VENN E COMBINAÇÕES

album_set_1={'ac/dc','black in black', 'thriller'}
album_set_2={'ac/dc','black in black', 'the dark side of the moon'}

#O SIMBOLO/COMANDO DE & SIGNIFICA A INTERSEÇÃO NOS DIAGRAMAS VENN
album_set_3=album_set_1&album_set_2
print(album_set_3)
#O NOVO DIAGRAMA SET3 CONTERÁ OS ELEMENTOS EXISTENTES AO MESMO TEMPO NOS DIAGRAM SET 1 E SET2

# O SIMBOLO/COMANDO UNION JUNTARÁ TODOS OS ELEMENTOS E FARÁ UM DIAGRAMA ÚNICO COM TODOS OS ELEMENTOS, UM "MEGA SET"
album_set_1.union(album_set_2)

# ISSUBSET = quando os elementos de um diagrama menor estão contidos em um diagrama maior
album_set1={'acdc', 'black in black', 'thriller'}
album_set3={'acdc', 'black in black'}
album_set3.issubset(album_set1)

album_set4=album_set_2.intersection(album_set_1)
print(album_set4)
album_set_3.intersection(album_set_2)


#CONDIÇÕES E COMPARAÇÕES

#o sinal de igual = torna Elementos correspondentes/iguais.
a=6
# o sinal == compara se os valores são correspondentes, é uma pergunta, se os elementos são iguais.
6==7
#o resultado é falso.
6==6
#o resultado é true.
# 1=2 --> isso é um erro de sintaxe. 

i=6
i>5
i>=5
i<2
i=5
i>=5
i=2
i>=5
i<6
# se usar o signal de != estamos pedindo o valores diferentes, i sinal de = significa NÃO
# ou seja, != significa "não é igual a..."

i=2
i!=6
#o resultado será true 
i!=2
#o resultado será falso, pois 2 é igual a 2, != é um operador de desigualdade
5!=5
#resultado é false 
"ac/dc"=="Michael Jackson"
"ac/dc"!="Michael Jackson"

#OBS.: Python faz DIFERENÇA entre LETRAS MAIUSCULAS E MINUSCULAS
#EX.: 'a'=='A' --> false


#CONDIÇÃO: if , else, elif 

x="A"
if(x=="A"):
  print('hello')
else:
  print('hi')

#PARA IR AO SHOW DO AC/DC O INDIVÍDUO PRECISA SER MAIOR DE 18
age=18 #18 ou outro número
if(age>18):
    print("you can enter")
print('move on')

#se o indivíduo lançar (tiver idade) age=17, o sistema voltará com MOVE ON, se lançar age=19 ou mais o
#sistema voltará com TRUE e após YOU CAN ENTER.
#SE IND. IGUAL OU MENOR DE 18, FALSE, MOVE ON.

 #   PODE-SE ADICIONAR OUTRA CONDIÇÃO DE RESULTADO, com ELSE, os individuos poderão ter acesso ou não 
  #  ao primeiro E TAMBÉM AO UM SEGUNDO.
#SE O INDIVIDUO É MAIOR DE 18 ELE TERÁ ACESSO AO SHOW DO AC/DC E AO MEAT LOAF, SE MENOR DE 18 NÃO TERÁ ACESSO AO 
#SHOW DO AC/DC MAS PODERÁ ACESSAR O MEAT LOAF

#age coloca-se = e o número
if(age>18):
    print("you can enter")
else:
  print("go see Meat Loaf")
print("move on")
#SE MAIOR DE 18 YOU  CAN ENTER  is True E APÓS MOVE ON
#SE IGUAL OU MENOR DE 18 RESULT. IS false, e ACESSO AO MEAT LOAF. PRINT EM MOVE ON 

# ELIF = ELSE IF "MAS SE..." OU "SÓ SE..."

if(age>18):
  print('you can enter')
elif(age==18):
  print('go see Pink Floyd')
else:
    print("go see Meat Loaf")
print('move on')
 #IND COM 18, A 1ª COND É FALSE, E A SEGUNDA COND É TRUE, e ao final MOVE ON.
 # SE IND. COM 17, FALSE, FALSE E "GO SEE MEAT LOAF"
 # SE IND COM 19 OU MAIS, TRUE e MOVE ON.

#LOGIC OPERATORS
# OR 
# f+f=f
# f+t=t 
# t+f=t
# t+t=t
#OPERADOR OR SÓ SERÁ FALSE SE TODOS OS ELEMENTOS FOREM FALSOS

album_year=1990
if (album_year<1980) or (album_year>1989):
    print("the album was made in the 70's ou 90's")
else:
    print("the album was made in the 1980's")

# AND 
# F+F=False
# F+T=False
# T+F+False
# T+T=True
#SÓ SERÁ VERDADEIRO/ TRUE SE TODOS OS ELEMENTOS FOREM VERDADEIROS

album_year=1983
if(album_year>1979) and (album_year<1990):
    print("this album was made in the 80's")
#SE O VALOR FOR FALSO O SISTEMA RODA DIRETO E NÃO DEVOLVE RESULTADO

#LOOPS --> EXECUTA O BLOCO DE INFORMAÇÕES REPETIDAS VEZES ATÉ ENCONTRAR UMA CONDIÇÃO TRUE. 
#FOR, WHILE 
#RANGE É A O ALCANCE / SÉRIE/ VARIAÇÃO 
#EX.: 
range(3)
range(0,3)
range(1,3)
range(10,15)

#FOR 
for x in range(0,3):
    print(x,0)

for i in ['a','b','c']:
    print(i+'a')

for i,x in enumerate(['a','b','c']):
  print(i,x)

squares=['orange','orange','purple','orange','blue']
newsquares=[]
i=0
while(squares[i]=='orange'):
    newsquares.append(squares[i])
 #o loop acima rodará infinitamente, até que algo aconteça e o array não satisfaça mais as condições iniciais.

a=['1','2','3']
for i in a:
    print(2*i)

for i in range(1,5):
  if (i!=2):
    print(i)

album_ratings=[10.0,8.5,9.5,7,7,9.5,9.0,9.5]
L=len(album_ratings)
print(L)

def add1(x):
    b=x+1
    return b
add1(5)
def Print(A):
  for a in A:
    print(a+'1')
Print(['a','b','c'])

#RASCUNHO DO PRIMEIRO PROJETO:
ALTURA = float(input('qual é sua altura em centimetros?:'))

PESO =  float(input('qual é o seu peso?, sem mentir heim:'))

IMC= PESO//(ALTURA/100)**2

if IMC < 18.5:

  print(f'vc está só a capa do Batman, imc de {IMC}, muito abaixo do peso heim.')
elif IMC >=18.5 and IMC<=24.9:
    print(f'tá de boa, imc de {IMC}, peso normal.')
elif IMC >=25 and IMC <=29.9:
    print(f'tá ficando gordinho já heim, imc de {IMC}, sobrepeso.')


#FOR in list
squares=['red','yellow','green','purple','blue'] #this is a list
for i in range(0,5):
    squares[1]='white'
    print(squares) #it changes yellow to white in the list
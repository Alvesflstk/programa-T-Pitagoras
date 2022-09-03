from math import hypot
from emoji import emojize

num2: str = input('''Digite 
[1] para calcular a Hipotenusa.
[2] para calcular o cateto oposto .
[3] para calcular o cateto adjacente. 
 ''')

if '1' in num2:
    co = float(input('Digite o Comprimento Do Cateto Oposto: '))
    ca = float(input('Digite o Comprimento do cateto Adjacente: '))
    hi = hypot(co, ca)
    print(emojize("o sua Hipotenusa será {:.2f} :red_triangle_pointed_up: ".format(hi)))
    f = input( 'Digite [0] para retornar ao menu ou [5]finalize o programa' )

elif '2' in num2:
    c1 = float(input('Digite sua hipotenusa: '))
    c2 = float(input('Digite seu Cateto Adjacente: '))
    ct = c1**2 - c2**2
    print(emojize("o seu cateto oposto será {:.2f} :red_triangle_pointed_up: ".format(ct)))
    f = input( 'Digite [0] para retornar ao menu ou [5]finalize o programa' )

elif '3' in num2:
    c3 = float(input('Digite sua hipotenusa: '))
    c4 = float(input('Digite seu Cateto Oposto: '))
    ct2 = c3 ** 2 - c4 ** 2
    print(emojize("o seu cateto Adjacente será {:.2f} :red_triangle_pointed_up: ".format(ct2)))
    f = input( 'Digite [0] para retornar ao menu ou [5]finalize o programa' )
if '0' in f:
    num2: str = input( '''Digite 
[1] para calcular a Hipotenusa.
[2] para calcular o cateto oposto .
[3] para calcular o cateto adjacente. 
 ''' )

    if '1' in num2:
        co = float( input( 'Digite o Comprimento Do Cateto Oposto: ' ) )
        ca = float( input( 'Digite o Comprimento do cateto Adjacente: ' ) )
        hi = hypot( co, ca )
        print( emojize( "o sua Hipotenusa será {:.2f} :red_triangle_pointed_up: ".format( hi ) ) )
        f = input( 'Digite [0] para retornar ao menu ' )


    elif '2' in num2:
        c1 = float( input( 'Digite sua hipotenusa: ' ) )
        c2 = float( input( 'Digite seu Cateto Adjacente: ' ) )
        ct = c1 ** 2 - c2 ** 2
        print( emojize( "o seu cateto oposto será {:.2f} :red_triangle_pointed_up: ".format( ct ) ) )



    elif '3' in num2:
        c3 = float( input( 'Digite sua hipotenusa: ' ) )
        c4 = float( input( 'Digite seu Cateto Oposto: ' ) )
        ct2 = c3 ** 2 - c4 ** 2
        print( emojize( "o seu cateto Adjacente será {:.2f} :red_triangle_pointed_up: ".format( ct2 ) ) )





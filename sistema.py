# menu prinicpal
# autor jose luis programa costo a 300 pesos
import sys

def factura():
    IGV = (sumatotal) * 0.18
    total_pagar = sumatotal + IGV
    print(f"""
    |================================|
    |        FACTURA DE COMPRA       |
    |================================|
    |  Subtotal:        {sumatotal}          |
    |  IGV:          {round(IGV,2)}             |
    |  Total a pagar: {total_pagar} $          |
    |================================|""")

def menu():
    global pedido, continuar, a, b, c, d, e, f, g, cont, sumatotal
    continuar = True
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    sumatotal = 0
    while True:
        print(""""
        |=================================|
        |         RESTAURANTE S.A         |
        |              MENU               |
        |=================================|
        | A |Desayuno                     |
        | B |Almuerzo                     |
        | C |Cena                         |
        |=================================|
        | D |========= SALIR =============|
        |=================================|
        """)
        print("""""");
        opcion = input("Seleccionar opcion")
        print("""""")

        if opcion == "A":
            while continuar:
                print("""
                |            DESAYUNO             |
                |=================================|
                | Producto                |precio |
                | 1 |Cafe                 |S/4.50 |
                | 2 |Chocolate            |S/5.00 |
                | 3 |Jugo de fresas       |S/9.00 |
                | 4 |Jugo de papaya       |S/8.00 |
                | 5 |Pna con pollo        |S/7.00 |
                | 6 |Pan con jamon        |S/7.00 |
                | 7 |Pan con tortilla     |S/7.00 |
                | 8 |========= SALIR =============|
                |=================================|
                             
                             """)
                print("""""")
                desayuno = int(input("QUE DESEA?"))
                print("""""")
                pedido = str('su pedido ha sido: ')
                if desayuno == 1:
                    c1 = c1 + 1
                    cafe = 4.50 * c1
                    print(f"{pedido} CAFÉ")
                    a = cafe
                elif desayuno == 2:
                    c2 = c2 + 1
                    cho = 5.00 * c2
                    print(f"{pedido} CHOCOLATE")
                    # suma = suma + cho
                    b = cho
                elif desayuno == 3:
                    c3 = c3 + 1
                    jf = 9.00 * c3
                    print(f"{pedido} JUGO DE FRESA")
                    # suma = suma + jf
                    c = jf
                elif desayuno == 4:
                    c4 = c4 + 1
                    jp = 8.00 * c4
                    print(f"{pedido} JUGO DE PAPAYA")
                    d = jp
                elif desayuno == 5:
                    c5 = c5 + 1
                    pp = 7.00 * c5
                    print(f"{pedido} PAN CON POLLO")
                    e = pp
                elif desayuno == 6:
                    c6 = c6 + 1
                    paj = 7.00 * c6
                    print(f"{pedido} PAN CON JAMON")
                    f = paj
                elif desayuno == 7:
                    c7 = c7 + 1
                    pt = 7.00 * c7
                    print(f"{pedido} PAN CON TORTILLA")
                    g = pt

                sumatotal = a + b + c + d + e + f + g
                factura()

                if desayuno != 0:
                    resp = input('¿Deseas ordenar otras cosa o salir ? ')
                    if resp == 'Y' or resp == 'y':
                        pass
                    else:
                        continuar = False


        elif opcion == "B":
            while continuar:
                print("""
                |            ALMUERZO             |
                |=================================|
                | Producto                |precio |
                | 1 | Ensala de atún      |S/9.50 |
                | 2 | Tallarines verdes   |S/7.50 |
                | 3 | Arroz con pollo     |S/6.00 |
                | 4 | Ceviche             |S/6.00 |
                | 5 | Estofado  de carne  |S/5.50 |
                | 6 | Pollo a la parrilla |S/4.00 |
                | 0 |========= SALIR =============|
                |=================================|        
                """)
                print("""""")
                almuerzo = int(input("QUE DESEA?"))
                print("""""")
                pedido = str('su pedido ha sido: ')
                if almuerzo == 1:
                    c1 = c1 + 1
                    ea = 9.50 * c1
                    print(f"{pedido} ENSALADA DE ATUN")
                    a = ea
                elif almuerzo == 2:
                    c2 = c2 + 1
                    tv = 7.50 * c2
                    print(f"{pedido} TALLARINES VERDES")
                    b = tv
                elif almuerzo == 3:
                    c3 = c3 + 1
                    ap = 6.00 * c3
                    print(f"{pedido} ARROZ OCN POLLO")
                    c = ap
                elif almuerzo == 4:
                    c4 = c4 + 1
                    ce = 6.00 *c4
                    print(f"{pedido} CEVICHE")
                    d = ce
                elif almuerzo == 5:
                    c5 = c5 + 1
                    ec = 5.50 * c5
                    print(f"{pedido} ESTOFADO DE CARNE")
                    e = ec
                elif almuerzo == 6:
                    c6 = c6 + 1
                    pop = 4.00 * c6
                    print(f"{pedido} POLLO A LA PARRILLA")
                    f = pop
                sumatotal = a + b + c + d + e + f
                factura()

                if almuerzo != 0:
                    resp = input('¿Deseas ordenar otras cosa o salir ? ')
                    if resp == 'Y' or resp == 'y':
                        pass
                    else:
                        continuar = False

        elif opcion == "C":
            while continuar:
                print("""      
                |            CENA             |
                |=================================|
                | Producto                |precio |
                | 1 | Pizza exprés        |S/9.50 |
                | 2 | Ensalada campera    |S/7.50 |
                | 3 | Gazpacho            |S/6.00 |
                | 4 | Pollo al horno      |S/5.50 |
                | 5 | Menestrón           |S/4.00 |
                | 0 |========= SALIR =============|
                |=================================|
                                """)
                print("""""")
                cena = int(input("QUE DESEA?"))
                print("""""")
                pedido = str('su pedido ha sido: ')
                if cena == 1:
                    c1 = c1 + 1
                    pe = 9.50 *c1
                    print(f"{pedido} PIZZA EXPRES")
                    a = pe
                elif cena == 2:
                    c2 = c2 + 1
                    en = 7.50 * c2
                    print(f"{pedido} ENSALA CAMPERA")
                    b = en
                elif cena == 3:
                    c3 = c3 + 1
                    ga = 6.00 *c3
                    print(f"{pedido} GAZPACHO")
                    c = ga
                elif cena == 4:
                    c4 = c4 + 1
                    ph = 5.50 *c4
                    print(f"{pedido} POLLO AL HORNO")
                    d = ph
                elif cena == 5:
                    c5 = c5 + 1
                    me = 4.00 * c5
                    print(f"{pedido} MENESTRON")
                    e = me

                sumatotal = a + b + c + d + e
                factura()

                if cena != 0:
                    resp = input('¿Deseas ordenar otras cosa o salir ? ')
                    if resp == 'Y' or resp == 'y':
                        pass
                    else:
                        continuar = False

        else:
            print("""
             .----------------------------.
             |        gracias !!!!        |
             .----------------------------.""")
            sys.exit()

menu()

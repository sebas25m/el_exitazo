"""
    @author Sebastian Montoya Rosario
    Fecha de creación: 8/08/2023
    Funcionalidad: Este programa pide los datos del usuario para un almacén, luego le pregunta cuantos
    productos desea comprar y le da el total de la compra.
"""
import time
import yaml as ym

pdct_canasta = ("pan", "leche", "huevos", "arroz", "queso", "carne", "pollo", "fruta", "verdura", "tuberculo")
categorias = ['Frutas y vegetales', "Cárnicos", "Lacteos", "Enlatados", "Snacks", "Bebidas", "Cuidado personal",
              "Productos de aseo"]
sub_categorias = {"Frutas": {"limon - 1500 gr - $3.500": 3500,
                             "Banano - 1 unidad - $700": 700,
                             "Piña golden - 1  unidad - $13.000": 13000,
                             "Mango - 1 unidad - $6.100": 6100,
                             "Naranja tangelo - 1 unidad - $2.300": 2300,
                             "Manzana - 1 unidad - $4.800": 4800},
                  "Vegetales": {"Tomate - 1 unidad - $1.700": 1700,
                                "Cebolla - 1 unidad - $2.000": 2000,
                                "Aguacate - 1 unidad - $1.600": 1600,
                                "Pimenton - 1  unidad - $800": 800,
                                "Platano - 1 unidad - $2.200": 2200,
                                "Ajo - 10gr - $4.400": 4400},
                  "Tuberculos": {"Papa pastusa - 1 kilo - $12.000": 12000,
                                 "Papa criolla - 500 gr - $8.500": 8500,
                                 "Yuca - 500gr - $5.600": 5600,
                                 "Arracacha - 250 gr - $2.700": 2700,
                                 "Cubios - 300 gr - $5.600": 5600},
                  "Carne": {"Corte rib-eye - 1 kilo - $30.000": 30000, "Tocino - 500gr - $20.000": 20000,
                            "Milanesa de cerdo - 500 gr - $15.500": 15500,
                            "Costillas de res - 1 kilo - $25.000": 25000, "Lomo de cerdo - 500gr - $8900": 8900},
                  "Pollo": {"Pollo despresado - 1 kilo - $28000": 28000, "Pechuga - 500 gr - $12.000": 12000,
                            "Milanesa de pollo - 500 gr - $12.100": 12100, "Perniles de pollo - 500 gr - $12000": 12000,
                            "Alitas de pollo - 1 kilo - $14.900": 14900},
                  "Pescados y mariscos": {"Filete de salmon - 500 gr - $35.900": 35900,
                                          "Trucha - 500 gr - $8.100": 8100,
                                          "Filete de tilapia - 500 gr - $9.200": 9200,
                                          "Camaron tigre - 500 gr - $35.100": 35100,
                                          "Palmitos - 1 kilo - $29.000": 29000,
                                          "Langostinos - 500 gr - $35.200": 35200},
                  "Quesos": {"Queso campesino bloque - 250 gr - $6.800": 6800,
                             "Queso campesino tajado - 250 gr - $7.500": 7500,
                             "Queso mozzarella tajado - 500 gr - $12.900": 12900,
                             "Queso doble crema bloque - 250 gr - $6.300": 6300,
                             "Queso semi-descremado bloque - 250 gr - $7.800": 7800,
                             "Queso descremado tajado - 250 gr - $8.000": 8000},
                  "Lacteos": {"Paca de leche  - 6 unidades - $24.900": 24900,
                              "Leche corriente - 1 l - $3.900": 3900,
                              "Yogurt de mora - 1 l - $4.300": 4300,
                              "Yogurts surtidos - 6 unidades de 100 ml c/u - $14.900": 14900,
                              "Kumis - 1 litro - $7.500": 7500,
                              "Leche deslactosada - 1 litro - $4.800": 4800},
                  "Enlatados": {"Atún en agua - 200gr - $4.980": 4980,
                                "Atún en aceite - 640gr - $27.000": 27000,
                                "Aceitunas - 250gr - $5.200": 5200,
                                "Duraznos en almíbar - 820gr - $9.890": 9890,
                                "Frijoles enlatados - 400 gr - $7.700": 7700,
                                "Maiz tierno - 300 gr - $9.900": 9900},
                  "Embutidos": {"Salchichas de cerdo - 1 docena - $13.600": 13600,
                                "Salchicha hot-dog - 8 unidades - $15.800": 15800,
                                "Chorizos - 6 unidades - $17.400": 17400,
                                "Morcilla - 7 unidades - $17.400": 17400,
                                "Chorizo coctel - 8 unidades - $14.500": 14500,
                                "Salchichas del rancho - 5 unidades - $6.200": 6200},
                  "Frituras": {"Papas fritas - 120gr - $3.500": 3500,
                               "Todo rico - 120 gr - $2.800": 2800,
                               "De todito - 125gr - $3.200": 3200,
                               "Papas fritas - 380 gr - $7.500": 7500,
                               "Todo rico - 380gr - $8.200": 8200,
                               "De todito - 400 gr - $8.000": 8000},
                  "Confitería": {"Chocolatina Jetix - 144 gr - $7.980": 7900,
                                 "Chocolatina jumbex - 144 gr - $8.500": 8500,
                                 "Gomitas Trulutolix - 100 gr - $3.400": 3400,
                                 "Chicles Trihalls - 10 unidades - $4.500": 4500,
                                 "Paquete de moritas - 20 unidades - $9.300": 9300},
                  "frutos secos": {"Arándanos - 500 gr - $6.700": 6700, "Mani - 300 gr - $5.100": 5100,
                                   "Avellanas - 150 gr - $5.900": 5900, "Almendras - 200 gr - $4.500": 4500,
                                   "Nueces - 180 gr - $4.300": 4300},
                  "Licores": {"Six-pack BBC - 6 unidades - $20.900": 20900,
                              "Medio litro de aguardiente - 500ml - $45.000": 45000,
                              "Whiskey Buchanan´s 18 años - 1 l - $200.000": 200000,
                              "Absolute vodka - 500 ml - $88.000": 88000,
                              "Whiskey old parr - 300ml - $110.000": 110000},
                  "refrescos": {"Cola-coca - 1.5 l - $5.800": 5800, "Up-seven - 1.5 l - $4.900": 4900,
                                "Panela-limonada - 6 unidades - $7.500": 7500,
                                "panelimonada - 1 unidad - $1.300": 1300, "Gaseosa genérica - 1.2 l - $2.900": 2900},
                  "Productos de belleza": {"Paleta de sombras - 8 colores - $230.000": 230000,
                                           "Paleta de sombras - 6 colores - $193.900": 193900,
                                           "Fijador para cejas - 7 ml - $123.900": 123900,
                                           "Pomada para cejas - color: negro - $13.000": 1300},
                  "Productos para bebe": {"Pañales - 64 unidades - $78.000": 78000,
                                          "Pañitos húmedos - 120 pañitos - $45.900": 45900,
                                          "Crema - 100 ml - $15.000": 15000,
                                          "Pañitos secos - 60 unidades - $39.900": 39900, },
                  "limpieza general para el hogar": {"Jabón limpia pisos - 1 l - $9.800": 9800,
                                                     "Jabón en polvo - 4 kg - $34.800": 34800,
                                                     "Jabón en barra - 2 unidades - $19.900": 12900,
                                                     "Jabón liquido - 1.5 l - $54.900": 54900,
                                                     "Papel higiénico - 12 unidades - $49.800": 49800},
                  "Aseo personal": {"Jabón corporal - 6 unidades - $12.900": 12900,
                                    "Jabón para manos - 500 ml - $15.900": 15900,
                                    "Crema para manos - 1 l - $31.000": 31000,
                                    "Bloqueador UV-50 FPS - 700 ml - $27.000": 27000,
                                    "Desodorante - 2 unidades - $15.900": 15900}
                  }
user_canf = []
user_pdct = []
prc1_pdct = []
prc_total = []
subtotal = 0
solic_datos = ["Escriba su nombre completo: ", "Ingrese su numero de documento: ", "Ingress su edad: ",
               "Ingrese su numero telefónico: ",
               "Ingrese su dirección de vivienda: ", "Ingrese su e-mail: ",
               "Cree una contraseña: "]
datos_User = []
nombres_User = []
global esNumero
global opc
global k


def pr_sub_cat(inicio, fin):
    k = 0
    for i in list(sub_categorias.keys())[inicio:fin]:
        k += 1
        print(f"{k}. {i}")
    while True:
        opc = input("Escribe el numero según la categoria a la que quieras ingresar: ")
        if check_num(opc):
            break
        else:
            continue
    return opc


def pr_products(indice):
    k = 0
    for i in list(sub_categorias.values())[indice]:
        k += 1
        print(f"{k}. {i}")
    while True:
        opc = input("Escribe el numero del producto que quieres comprar: ")
        if chek_num(opc):
            break
        else:
            continue


def check_num(valor):
    """
    Esta función evalúa si los Strings contienen válores numéricos o no, si el string es de solo números arroja 'True',
    de lo contrario arroja 'False' para que una condición no se cumpla
    :param valor:
    :return esNumero:
    """
    partition = valor.partition('.')
    if valor.isdigit():
        esNumero = True

    elif (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (
            partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (
            partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
        esNumero = True
    else:
        esNumero = False
    return esNumero


def recopilar_Datos():
    """
        Esta función lee la información del usuario y la guarda en la lista 'datos_user[]'
    :return lista datos_User:
    """
    nombre = input(solic_datos[0])
    datos_User.extend(nombre.split())
    for i in range(len(solic_datos) - 1, 0, -1):
        datos_User.append(input(solic_datos[len(solic_datos) - i]))
    return datos_User


def editar_Datos():
    """
    En esta función el usuario podrá editar la información de su cuenta
    :return:
    """

    while True:
        print("Confirme sus datos: ")
        if len(datos_User) == 9:
            print(f"Primer nombre: {datos_User[len(datos_User) - 9]}")
            print(f"Primer apellido: {datos_User[len(datos_User) - 8]}")
            print(f"Segundo apellido: {datos_User[len(datos_User) - 7]}")
            print(f"Numero de documento: {datos_User[len(datos_User) - 6]}")
            print(f"Edad: {datos_User[len(datos_User) - 5]}")
            print(f"Numero de teléfono: {datos_User[len(datos_User) - 4]}")
            print(f"Dirección: {datos_User[len(datos_User) - 3]}")
            print(f"E-mail: {datos_User[len(datos_User) - 2]}")
            print(f"Contraseña: {datos_User[len(datos_User) - 1]}")
        else:
            print(f"Primer nombre: {datos_User[len(datos_User) - 10]}")
            print(f"Segundo nombre: {datos_User[len(datos_User) - 9]}")
            print(f"Primer apellido: {datos_User[len(datos_User) - 8]}")
            print(f"Segundo apellido: {datos_User[len(datos_User) - 7]}")
            print(f"Numero de documento: {datos_User[len(datos_User) - 6]}")
            print(f"Edad: {datos_User[len(datos_User) - 5]}")
            print(f"Numero de teléfono:  {datos_User[len(datos_User) - 4]}")
            print(f"Dirección: {datos_User[len(datos_User) - 3]}")
            print(f"E-mail: {datos_User[len(datos_User) - 2]}")
            print(f"Contraseña: {datos_User[len(datos_User) - 1]}")
        opc_editar = input("Escribe 1 para editar algún dato ó 2 para confirmas los datos: ")
        if opc_editar == "1":
            opc_editar = input(
                "1. Editar nombre\n2. Editar numero de documento\n3. Editar edad\n4. Editar numero de teléfono\n5. "
                "Editar dirección\n6. Editar E-mail\n7. Editar contraseña")
            if opc_editar == "1":
                input("""Escriba según lo que quiera realizar: \n1. Editar primer nombre 
                    \n2. Editar primer nombre \n3. Editar primer nombre \n4. Editar primer nombre""")
            elif opc_editar == "2":
                datos_User.insert(len(datos_User) - 6, input(solic_datos[1]))
            elif opc_editar == "3":
                datos_User.insert(len(datos_User) - 5, input(solic_datos[2]))
            elif opc_editar == "4":
                datos_User.insert(len(datos_User) - 4, input(solic_datos[3]))
            elif opc_editar == "5":
                datos_User.insert(len(datos_User) - 3, input(solic_datos[4]))
            elif opc_editar == "6":
                datos_User.insert(len(datos_User) - 2, input(solic_datos[5]))
            elif opc_editar == "7":
                datos_User.insert(len(datos_User) - 1, input(solic_datos[6]))
        elif opc_editar == "2":
            print("Datos confirmados.\nIngresando a el exitazo.")
        else:
            print("Numero de opción incorrecta.")
            continue
    return datos_User


def product_canasta(product_name):
    for canasta_product in pdct_canasta:
        if canasta_product in product_name:
            return True
    return False


def comprar_Productos():
    """
    En esta función el usuario podrá comprar los productos
    :return:
    """
    global subtotal, primer_diccionario
    k = 0
    for i in categorias:
        k += 1
        print(f"{k}. {i}")
    while True:
        opc = input("Escribe el numero según la categoria a la que quieras ingresar: ")
        if check_num(opc):
            if opc == "1":
                pr_sub_cat(0, 3)
                break
            elif opc == "2":
                pr_sub_cat(3, 6)
                break
            elif opc == "3":
                pr_sub_cat(6, 8)
                break
            elif opc == "4":
                pr_sub_cat(8, 11)
                break
            elif opc == "5":
                pr_sub_cat(11, 13)
                break
            elif opc == "6":
                pr_sub_cat(13, 15)
                break
            elif opc == "7":
                pr_sub_cat(15, 17)
                break
    return subtotal


def main():
    """Contextualizamos al usuario sobre la función del programa."""
    print("""\t\t\t\t\t\t\t\t  Bienvenido a almacenes el exitázo. 
        \nEste programa va a requerir de tus datos personales y también 
        la información de los productos que deseas comprar.
        \nAl final te dirá el total de lo que debes pagar.""")
    time.sleep(1.2)
    #    recopilar_Datos()
    #   editar_Datos()
    comprar_Productos()


main()

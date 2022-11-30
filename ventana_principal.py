import tkinter
from tkinter import *
from tkinter import Tk, Label, Button
from tkinter import messagebox as mb
from tkinter import scrolledtext
from tkinter.font import Font

import pyttsx3
import speech_recognition as sr


def v1():
    global v1
    v1 = Tk()
    v1.iconbitmap("vozz.ico")
    v1.config(bg="#FFFFFF")
    v1.resizable(0, 0)
    v1.attributes("-toolwindow", -1)
    v1.title("Proyecto IA- Mejorar el Habla")
    img = PhotoImage(file="hablar.png")
    label = Label(image=img).place(x=20, y=60)
    estilofuente = Font(family="Fredoka One", size=35)
    estilo = Font(family="Jetbrains mono", size=14)
    label = Label(text="Puedes hablar mas no ", font=estilofuente,
                  fg="black", bg="white").place(x=570, y=120)
    label = Label(text="comunicar", font=estilofuente,
                  fg="black", bg="white").place(x=570, y=185)
    label = Label(text="!!Aprendamos a Comunicar", font=estilofuente,
                  fg="red", bg="white").place(x=570, y=250)

    wtotal = v1.winfo_screenwidth()
    htotal = v1.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 1200
    hventana = 650
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal / 2 - wventana / 2)
    pheight = round(htotal / 2 - hventana / 2)
    #  aplicamos a la geometría de la ventana
    v1.geometry(
        str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))

    oton_cerrar = Button(v1,
                         text="Salir del Programa",
                         background="#34495E",
                         foreground="white",
                         font=estilo,
                         command=v1.destroy).place(x=800, y=500)
    boton_abrir = Button(v1,
                         text="Comenzar Leccion",
                         background="#aa0000",
                         foreground="white",
                         font=estilo,
                         command=v2).place(x=580, y=500)
    instruc = Button(v1, text="Intrucciones", background="#3498DB", foreground="white", command=v3, font=estilo)
    instruc.place(x=1000, y=10)
    print("dd", boton_abrir)

    v1.mainloop()


def v3():
    v3 = Toplevel()
    v3.iconbitmap("vozz.ico")
    v3.config(bg="#FFFFFF")
    v3.title("Instrucciones")
    v3.resizable(0, 0)
    v3.attributes("-toolwindow", -1)
    textoins = "Como usar? \n\n\n 1.- presionar comezar leccion- eso le llevara a otra ventana hacer sus pruebas \n\n " \
               "2.- cuando este en la segunda ventana presione el boton capturar voz \n\n  " \
               "    le saldra un mensaje de grbando darle en ok y inmediatamente comenzar a leer el texto\n\n  " \
               "    no importa si lo lee todo basta con el primer parrafo es suficiente \n\n  " \
               "    cuando termine de leer esperar unos segundos para procesar la vox y presionar \n\n  " \
               "    resultados eso le dira si lee rapido, lento o normal asi para mejorar su comunicacion\n\n   "
    ins = Label(v3, text=textoins, anchor="nw", borderwidth=1, relief="solid", justify=LEFT,
                font=("Verdana", 10))
    ins.place(x=10, y=10)
    estilo = Font(family="Jetbrains mono", size=12)
    exit = Button(v3, text="ok", background="red", foreground="white", font=estilo, width=10, command=v3.destroy)
    exit.place(x=516, y=300)
    wtotal = v3.winfo_screenwidth()
    htotal = v3.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 633
    hventana = 350
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal / 2 - wventana / 2)
    pheight = round(htotal / 2 - hventana / 2)
    #  aplicamos a la geometría de la ventana
    v3.geometry(
        str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    v3.mainloop()


def v2():
    global v2
    v2 = Tk()
    v2.iconbitmap("vozz.ico")
    v2.title("FUNCIONES DEL USUARIO")
    v2.resizable(0, 0)
    v2.config(bg="#F2F3F4")
    # estilo = Font(family="Jetbrainsmono 14 bold",size=14)
    captura = Label(v2, text="Captura de voz", fg="#333", font=("Arial 14 bold"))
    captura.place(x=15, y=10)

    captura1 = Label(v2, text="Texto de prueba", fg="#333", font=("Arial 14 bold"))
    captura1.place(x=350, y=10)

    cantidad_palabras = Label(v2, text="Cantidad de palabras leidas: ", font=("Arial 12 bold"), fg="#333", bg="#58D68D")
    cantidad_palabras.place(x=350, y=450)

    texto_largo = "Los relatos de  grandes viajeros como Jenófanes, Herodoto o el propio Alejandro Magno" \
                  " junto con la mitología, la política, la biología y otras áreas del conocimiento" \
                  "contribuyeron a la profunda reflexión sobre el origen del hombre, la sociedad y las diferencias " \
                  "entre unos pueblos y otros Los sofistas trataron de dar una explicación práctica al surgimiento" \
                  "de las sociedades, Sócrates y Platón propusieron la ética y los valores universales como explicación" \
                  "a esos fenómenos comunes en todos los pueblos, Aristóteles apostó por la biología haciendo" \
                  "de la sociedad y la cultura una carga inherente al ser humano. Epicúreos y estoicos centraron el origen" \
                  "social en el individuo y en su necesidad de bienestar.De esta primera experiencia sobre el debate antropológico" \
                  "podemos extraer una referencia  que va a marcar de manera  general la evolución" \
                  "de los estudios sobre las sociedades y las culturas: al hombre le satisface pensar" \
                  "sobre sí mismo y además este pensamiento es la clave que encamina a la resolución de" \
                  "algunos problemas de convivencia. Con el redescubrimiento de Aristóteles en el siglo XII, aparece  el hombre como " \
                  "ser dotado de razón, capaz de mejorar su propio destino y su condición social. Estas ideas crecieron en la obra de " \
                  "Santo Tomás de Aquino, quien  llegó a la conclusión de que el hombre se situaba en un escalón inmediatamente inferior al " \
                  "de los ángeles.  Sostuvo además la unidad psíquica del hombre,”por naturaleza todos los hombres son iguales“ otro de los " \
                  "paradigmas sobre los que la sociedad y en especial los gobiernos han interrogado a la antropología, especialmente en situaciones " \
                  "relacionadas con la esclavitud, el abuso de poder,  la emancipación de la mujer"

    txt_prueba = Text(v2, font=("Arial", 11), bg="#F8F9F9", fg="#333", relief=RIDGE, wrap=WORD, highlightcolor='green')
    txt_prueba.place(x=350, y=39, width=710, height=400)
    txt_prueba.insert(tkinter.END, texto_largo)
    txt_prueba.config(spacing2=5)
    txt_prueba.config(state='disabled')
    txt_prueba.bindtags((str(v2), str(v2), "all"))
    # txt_prueba = Label(v2, text=texto_largo, anchor="nw", borderwidth=1, relief="solid", justify=LEFT,
    #                    font=("verdana", 10), bg="white", width=90)
    # txt_prueba.place(x=350, y=39)
    # txt_prueba.focus()
    wtotal = v2.winfo_screenwidth()
    htotal = v2.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 1200
    hventana = 650
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse

    pwidth = round(wtotal / 2 - wventana / 2)
    pheight = round(htotal / 2 - hventana / 2)
    #  aplicamos a la geometría de la ventana
    v2.geometry(
        str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    if v2:
        v1.withdraw()
    engine = pyttsx3.init()
    # file_name = ("C:/Users/ADMIN/PycharmProjects/reconocer_voz/audio.wav")
    def voz_inicial():
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 130)
        engine.say("espere el mesaje de di algo para que puedas hablar")
        engine.runAndWait()

    def espera_res():
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 130)
        engine.say("espera, analizando tus resultados")
        engine.runAndWait()

    def captura():
        global cp
        cp = ""
        r = sr.Recognizer()
        with sr.Microphone() as source:
            voz_inicial()
            mb.showinfo("HABLA", "di algo")
            audio = r.listen(source)
            try:
                cp = r.recognize_google(audio, language="es-MX")
                print(cp)
                crear_archivo()
            except:
                pass
                mb.showinfo("ERROR", "No te escuche hablar")
            return cp

    def contar_palabras():
        global numeropalabras
        i = 0
        numeropalabras = 1
        while i < len(cp):
            if cp[i] == " ":
                numeropalabras = numeropalabras + 1
            i = i + 1
        print(f"cantidad de palabras es: {numeropalabras}")
        # simbolos = ['¿', '?', '.', '.', ';', ':', '¡', '!']
        # global numeropalabras
        # numeropalabras = 0
        # with open("C:/Users/ADMIN/PycharmProjects/reconocer_voz/grabado.txt", "r") as fichero:
        #     for linea in fichero:
        #         for simbolo in simbolos:
        #             linea = linea.replace(simbolo, " ")
        #         palabras = linea.split()
        #         for palabra in palabras:
        #             numeropalabras += 1
        # print(f"cantidad de palabras es: {numeropalabras}")
        return numeropalabras

    def crear_archivo():
        # f = open("C:/Users/ADMIN/PycharmProjects/reconocer_voz/grabado.txt", "w")
        # f.writelines(cp + "\n")
        # f.close()
        espera_res()
        res = Text(v2, font=("Arial 12 bold"), fg="#333", bg="#58D68D")
        res.insert(tkinter.END, contar_palabras())
        res.place(x=582, y=450, width=25, height=25)
        resultado()

        # leer_archivo()

    # def leer_archivo():
    #     archi = open("C:/Users/ADMIN/PycharmProjects/reconocer_voz/grabado.txt", "r")
    #     lee = archi.read()
    #     print(lee)
    #     archi.close()
    #     res = Text(v2, font=("Arial 12 bold"), fg="#333", bg="#58D68D")
    #     res.insert(tkinter.END, contar_palabras())
    #     res.place(x=582, y=450, width=25, height=25)
    #     resultado()
    # def clear_contador():
    #     global contador, contador2
    #     contador = 0
    #     # contador1 = 0
    #     contador2 = 0
    #
    # def formato(c):
    #     if c < 10:
    #         c = "0" + str(c)
    #     return c
    # hora, minutos, segundos, = 0, 0, 1
    #
    # def cuenta():
    #     global hora, minutos, segundos
    #     time['text'] = str(formato(hora)) + ":" + str(formato(minutos)) + ":" + str(formato(segundos))
    #
    #     if hora == 4:
    #         return
    #     segundos -= 1
    #     if segundos == 00:
    #         minutos -= 1
    #         segundos = 60
    #     if minutos == 00 and segundos == 00:
    #         hora += 1
    #
    #     time.config(text=f"{minutos:02}:{segundos:02}")
    #
    #     time.after(1000, cuenta)
    #
    # time = Label(v2, fg='green', width=20, text="00:00:00", bg="black", font=("", "20"))
    # time.place(x=682, y=450)


    # contador1 += 1

    # def tiempo_audio():
    #     with audioread.audio_open(file_name) as f:
    #         duracion = f.duration
    #         # muestreo, sonido = waves.read(archivo,"wr")
    #         # duracion = len(sonido) /muestreo
    #         # with contextlib.closing(wave.open(fname, 'r')) as f:
    #         #     frames = f.getnframes()
    #         #     velo = f.getframerate()
    #         #     duracion = frames / (velo)
    #         print("duracion", round(duracion))
    #     return duracion

    def resultado():
        T = 60
        vh = (contar_palabras() / T)
        if (vh <= 2.06666666667):
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            print(rate)
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 130)
            engine.say("hablas lento, esto podria aburrir a tu receptor te sugiero hacer otra prueba !!!")
            engine.runAndWait()

        elif (vh >= 2.08333333333 and vh <= 3.16666666667):
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            print(rate)
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 130)
            engine.say("esta es la forma correcta de hablar sigue a si!!!")
            engine.runAndWait()
        else:
            voices = engine.getProperty('voices')
            rate = engine.getProperty('rate')
            print(rate)
            engine.setProperty('voice', voices[0].id)
            engine.setProperty('rate', 130)
            engine.say("sabias que hablas muy rapido, tu receptor no te puede entender haz otra prueba por favor!!!")
            engine.runAndWait()
        print(f"ppm-:{vh}")

    # resss = Button(v2, text="res", compound=LEFT, activebackground="gold",
    #                bg="#2874A6", fg="white", font=("Arial 12 bold"), width=13,
    #                command=resultado)
    # resss.place(x=450, y=600)

    regresar = Button(v2, text="Regresar", command=volver_ventana, bg="#D35400", fg="white", font=("Arial 12 bold"),
                      width=10)
    regresar.place(x=950, y=600)

    capturar_audio = Button(v2, text="Capturar audio", compound=LEFT, activebackground="gold",
                            bg="#2874A6", fg="white", font=("Arial 12 bold"), width=13,
                            command=lambda: txt_area.insert(tkinter.END, captura()))
    capturar_audio.place(x=750, y=600)

    def reset():
        voices = engine.getProperty('voices')
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 130)
        engine.say("limpiando captura de voz para la siguiente prueba")
        engine.runAndWait()
        txt_area.delete(1.0, END)

    estilo2 = Font(family="Arial", size=12)
    txt_area = scrolledtext.ScrolledText(v2, font=estilo2, bg="white", fg="black", relief=GROOVE, wrap=WORD)
    txt_area.place(x=10, y=40, width=320, height=300)

    boton_reset = Button(v2, text="reset", command=reset, bg="#34495E", fg="white", font=("Arial 12 bold"), width=10)
    boton_reset.place(x=600, y=600)

    v2.mainloop()


def volver_ventana():
    global v2
    v1.iconify()
    v1.deiconify()
    v2.destroy()


v1()

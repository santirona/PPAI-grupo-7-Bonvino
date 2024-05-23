import os
from tkinter import *
from tkinter import font

class Principal:
    def __init__(self, master):
        self.master = master
        self.master.geometry('750x500')
        self.master.title('Grupo 7 - Bonvino - Aplicacion para enofilos - Principal')

        self.fuente_personalizable = font.Font(family='Helvetica', size=13, weight="bold", slant="italic")

        # Favicon de la Aplicación
        self.ico = os.path.abspath('./front/fotos/icono.ico')
        self.imagen_fondo_principal = os.path.abspath('./front/fotos/fondo_principal.png')

        try:
            self.icono = PhotoImage(file=self.ico)
            self.master.iconphoto(True, self.icono)
        except Exception as e:
            print(f"No se pudo cargar el icono: {e}")
            self.icono = None

        try:
            self.logo = PhotoImage(file=self.imagen_fondo_principal)
        except Exception as e:
            print(f"No se pudo cargar el fondo principal: {e}")
            self.logo = None

        # Sección #1 - Imagen
        self.seccion_logo = Frame(self.master, bg="#4b1a1a", width=300, height=500)
        self.seccion_logo.pack(side=LEFT, fill="both", expand=True)

        titulo_ventana = Label(self.seccion_logo, text="Bienvenido a Bonvino",
                               font=self.fuente_personalizable, pady=30, padx=20, bg="#4b1a1a", fg="white")
        titulo_ventana.pack()

        if self.logo:
            fondo_principal = Label(self.seccion_logo, image=self.logo, background="#4b1a1a", pady=20)
            fondo_principal.pack()

        # Sección #2 - Lista integrantes
        integrantes = Label(self.seccion_logo, text='Integrantes: ', bg="#4b1a1a", fg="white",
                            font=self.fuente_personalizable, pady=10)
        integrantes.pack()

        santiago = Label(self.seccion_logo, text='Orona, Santiago; Legajo: 95342 ', bg="#4b1a1a", fg="white",
                         font=self.fuente_personalizable, pady=2)
        santiago.pack()

        facundo = Label(self.seccion_logo, text='de la Fuente, Facundo; Legajo: 94798', bg="#4b1a1a", fg="white",
                        font=self.fuente_personalizable, pady=2)
        facundo.pack()

        angel = Label(self.seccion_logo, text='Rosales, Angel; Legajo: 95212', bg="#4b1a1a", fg="white",
                      font=self.fuente_personalizable, pady=2)
        angel.pack()

        emiliano = Label(self.seccion_logo, text='Diaz, Emiliano; Legajo: 95255', bg="#4b1a1a", fg="white",
                         font=self.fuente_personalizable, pady=2)
        emiliano.pack()

        julian = Label(self.seccion_logo, text='Bailey, Julián Eduardo; Legajo: 96032', bg="#4b1a1a", fg="white",
                       font=self.fuente_personalizable, pady=2)
        julian.pack()

        federico = Label(self.seccion_logo, text='de la Vega, Federico Agustin; Legajo: 95680', bg="#4b1a1a", fg="white",
                         font=self.fuente_personalizable, pady=2)
        federico.pack()

        mateo = Label(self.seccion_logo, text='Ramallo, Mateo; Legajo: 94441', bg="#4b1a1a", fg="white",
                      font=self.fuente_personalizable, pady=2)
        mateo.pack()

        # Sección #3 - Opciones de Administración
        self.seccion_opciones = Frame(self.master, borderwidth=2, relief="solid", bg="#361414", width=300, height=500)
        self.seccion_opciones.pack(side=RIGHT, fill="both", expand=True)

        titulo_opciones = Label(self.seccion_opciones, text="Menú de Opciones", font=self.fuente_personalizable,
                                pady=30, padx=60, bg="#361414", fg="white")
        titulo_opciones.pack()

        # Sección #4 - Botones
        botones = Frame(self.seccion_opciones)

        generar_ranking_vinos = Button(botones, text="Generar ranking vinos", fg="white", bg="#301212", 
                                       font=self.fuente_personalizable, width=20)
        generar_ranking_vinos.pack(fill="both", expand=True)

        test2 = Button(botones, text="Boton 2",fg="white", bg="#301212", 
                       font=self.fuente_personalizable, width=20)
        test2.pack(fill="both", expand=True)

        test3 = Button(botones, text="Boton 3", fg="white", bg="#301212", 
                       font=self.fuente_personalizable, width=20)
        test3.pack(fill="both", expand=True)

        test4 = Button(botones, text="Boton 4", fg="white", bg="#301212", 
                       font=self.fuente_personalizable, width=20)
        test4.pack(fill="both", expand=True)

        botones.pack(fill="both", expand=True)

    def mostrar(self):
        self.master.mainloop()

if __name__ == '__main__':
    root = Tk()
    ventana_principal = Principal(root)
    ventana_principal.mostrar()

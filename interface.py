from tkinter import *
import sistemas as m
import numpy as np

root = Tk()
root.geometry("800x500")
root.configure(bg='#F8F8FF')


def Salvar_Parametros():
    global kp
    global ki
    global kd
    global SP
    global PV
    global Ts
    global tempo2
    global tempo
    global a1
    global b1

    Theta = m.minimos_quadrados()

    a1 = Theta[0]
    b1 = Theta[1]

    kp = float(kpLabel.get())  # 13 Ganho proporcional
    ki = float(kiLabel.get())  # 0.5 Ganho integral
    kd = float(kdLabel.get())  # 1 Ganho derivativo

    SP = float(SPLabel.get())  # 50 Setpoint
    PV = float(PVLabel.get())  # 0 Precess Value

    Ts = float(tsLabel.get())  # 0.2 Tempo de amostragem
    tempo = float(xLabel.get())  # 350 Tempo do eixo x

    tempo2 = np.arange(0, tempo, Ts)


def Grafico_MA():  # Chama o grafico de malha aberta

    resposta_ma = m.malha_aberta(tempo2, a1, b1, PV, SP, Ts, tempo)
    m.grafico(tempo2, resposta_ma)


def Grafico_MF():  # Chama o grafico de malha fechada

    resposta_mf = m.malha_fechada_sem_ganho(tempo2, a1, b1, PV, SP, Ts, tempo)
    m.grafico(tempo2, resposta_mf)


def Grafico_MFG():  # Chama o grafico de malha fechada com controlador

    resposta_mfg = m.malha_fechada_controlador_PID(
        tempo2, a1, b1, PV, SP, kp, ki, kd, Ts, tempo)
    m.grafico(tempo2, resposta_mfg)


# ------------------primeiroContainer-------------------------------------------
fontePadrao = ("Arial", "10")

Container1 = Frame()
Container1["pady"] = 10
Container1["padx"] = 5
Container1["bg"] = '#F8F8FF'
Container1.pack()

Container2 = Frame()
Container2["pady"] = 10
Container2["padx"] = 5
Container2["bg"] = '#F8F8FF'
Container2.pack()

Container3 = Frame()
Container3["pady"] = 10
Container3["padx"] = 5
Container3["bg"] = '#F8F8FF'
Container3.pack()

Container4 = Frame()
Container4["pady"] = 10
Container4["padx"] = 5
Container4["bg"] = '#F8F8FF'
Container4.pack()

Container5 = Frame()
Container5["pady"] = 10
Container5["padx"] = 5
Container5["bg"] = '#F8F8FF'
Container5.pack()

Container6 = Frame()
Container6["pady"] = 10
Container6["padx"] = 5
Container6["bg"] = '#F8F8FF'
Container6.pack()

Container7 = Frame()
Container7["pady"] = 10
Container7["padx"] = 5
Container7["bg"] = '#F8F8FF'
Container7.pack()


cabecalho = Label(Container1, text="Sistemas Dinâmicos")
cabecalho["font"] = ("Arial", "14", "bold")
cabecalho["bg"] = '#F8F8FF'
cabecalho.pack()

titulo1 = Label(Container1, text="Parâmetros")
titulo1["font"] = ("Arial", "12", "bold")
titulo1["bg"] = '#F8F8FF'
titulo1.pack()

titulo2 = Label(Container6, text="Gerar Gráficos")
titulo2["font"] = ("Arial", "12", "bold")
titulo2["bg"] = '#F8F8FF'
titulo2.pack()

SPLabel = Label(Container2, text=" SP (Set Point) ",
                font=fontePadrao, bg='#F8F8FF')
SPLabel.pack(side=LEFT)

SPLabel = Entry(Container2)
SPLabel["bg"] = '#F8F8FF'
SPLabel["width"] = 10
SPLabel["font"] = fontePadrao
SPLabel.pack(side=LEFT)
SPLabel.insert(0, 50)

PVLabel = Label(Container2,
                text=" PV (Precess Value) ", font=fontePadrao, bg='#F8F8FF')
PVLabel.pack(side=LEFT)

PVLabel = Entry(Container2)
PVLabel["bg"] = '#F8F8FF'
PVLabel["width"] = 10
PVLabel["font"] = fontePadrao
PVLabel.pack(side=LEFT)
PVLabel.insert(0, 0)

tsLabel = Label(Container3,
                text=" Ts (Tempo de Amostragem) ", font=fontePadrao, bg='#F8F8FF')
tsLabel.pack(side=LEFT)

tsLabel = Entry(Container3)
tsLabel["bg"] = '#F8F8FF'
tsLabel["width"] = 10
tsLabel["font"] = fontePadrao
tsLabel.pack(side=LEFT)
tsLabel.insert(0, 0.2)

xLabel = Label(Container3,
               text=" Eixo x (Tempo(s)) ", font=fontePadrao, bg='#F8F8FF')
xLabel.pack(side=LEFT)

xLabel = Entry(Container3)
xLabel["bg"] = '#F8F8FF'
xLabel["width"] = 10
xLabel["font"] = fontePadrao
xLabel.pack(side=LEFT)
xLabel.insert(0, 350)

kpLabel = Label(Container4,
                text=" kp (Ganho Proporcional) ", font=fontePadrao, bg='#F8F8FF')
kpLabel.pack(side=LEFT)

kpLabel = Entry(Container4)
kpLabel["bg"] = '#F8F8FF'
kpLabel["width"] = 10
kpLabel["font"] = fontePadrao
kpLabel.pack(side=LEFT)
kpLabel.insert(0, 18)

kiLabel = Label(Container4,
                text=" ki (Ganho Integral) ", font=fontePadrao, bg='#F8F8FF')
kiLabel.pack(side=LEFT)

kiLabel = Entry(Container4)
kiLabel["bg"] = '#F8F8FF'
kiLabel["width"] = 10
kiLabel["font"] = fontePadrao
kiLabel.pack(side=LEFT)
kiLabel.insert(0, 7)

kdLabel = Label(Container4,
                text=" kd (Ganho Derivativo) ", font=fontePadrao, bg='#F8F8FF')
kdLabel.pack(side=LEFT)

kdLabel = Entry(Container4)
kdLabel["bg"] = '#F8F8FF'
kdLabel["width"] = 10
kdLabel["font"] = fontePadrao
kdLabel.pack(side=LEFT)
kdLabel.insert(0, 1)


btn_s = Button(Container5, text="Salvar Parametros", padx=50,
               pady=5, width=20, bg="#D35400", fg="white", command=Salvar_Parametros)
btn_s.pack()


btn_ma = Button(Container7, text="Malha Aberta", padx=50,
                pady=5, width=20, bg="DimGray", fg="white", command=Grafico_MA)
btn_ma.pack()


btn_mf = Button(Container7, text="Malha Fechada",
                padx=50, pady=5, width=20, bg="DimGray", fg="white", command=Grafico_MF)
btn_mf.pack()


btn_mfc = Button(Container7, text="Malha Fechada com Controlador PID",
                 padx=50, pady=5, width=20, bg="DimGray", fg="white", command=Grafico_MFG)
btn_mfc.pack()


root.mainloop()

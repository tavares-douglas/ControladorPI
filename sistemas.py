
import numpy as np
import matplotlib.pyplot as plt
from scipy import io, signal
from control import *

# --------------------------------Amostras----------------------------------


def grafico(tempo, y):  # Plota um gráfico
    plt.plot(np.arange(0, tempo, tempo/len(y)), y)
    plt.grid()
    plt.xlabel("tempo")
    plt.ylabel("y")
    plt.show()


def graficos(tempo, y1, y2, y3):  # Plota mais de um gráfico
    # print(tempo)
    # print(y1)
    plt.plot(np.arange(0, tempo, tempo/len(y1)), y1, color='green')
    plt.plot(np.arange(0, tempo, tempo/len(y2)), y2, color='red')
    plt.plot(np.arange(0, tempo, tempo/len(y3)), y3, color='blue')
    plt.grid()
    plt.xlabel("Tempo [s]")
    plt.ylabel("Y[m]")
    plt.title("Sistema Dinâmico")
    plt.show()

# ----------------------------------Malha Aberta-------------------------------------


def malha_aberta(tempoV, a1, b1, PV, SP, ts, tempo):
    resposta = []
    arange = list(np.arange(0, tempoV, ts))
    for i in arange:
        PV = a1*PV + b1*SP
        resposta.append(PV)
    return resposta
    #grafico(tempo, resposta)

# ----------------------------------Malha Fechada com Controlador PID-------------------------------------


def malha_fechada_sem_ganho(tempoV, a1, b1, PV, SP, Ts, Tempo):
    resposta = []
    for i in np.arange(0, Tempo, Ts):
        erro = SP - PV
        PV = a1*PV + b1*erro
        resposta.append(PV)
    return resposta
    #grafico(tempoV, resposta)

# ----------------------------------Malha Fechada com Controlador PID-------------------------------------


def malha_fechada_controlador_PID(tempoV, a1, b1, PV, SP, Kp, Ki, Kd, Ts, tempo):
    resposta = []
    acao_integral = 0

    erro_anterior = SP - PV
    for i in np.arange(0, tempo, Ts):  # o i vai de 0.1 até 100 passo 0.1

        erro = SP - PV

        acao_proporcional = Kp*erro
        acao_integral = acao_integral + Ki*Ts*erro
        acao_derivativa = ((erro - erro_anterior)/Ts)*Kd

        erro_anterior = erro

        acao_controlador = acao_proporcional + acao_integral + acao_derivativa

        PV = (a1*PV) + (b1*acao_controlador)
        resposta.append(PV)
    return resposta
    #grafico(tempoV, resposta)

# --------------------------------Mínimos Quadrados ----------------------------------


def minimos_quadrados():

    # Pegando as amostras de um  arquivo txt
    # degrau0_2 = open('degrau0_2.txt', 'r')
    # resp0_2 = open('resp0_2.txt', 'rb')
    # tempo0_2 = open('tempo0_2.txt', 'r')

    # Pegando a amostra direto em formato Matlab
    #  Tenho o vetor degrau0_2,  resp0_2 e tempo0_2 dentro da amostra
    mydata = io.loadmat('Dados_Grupo_8.mat')
    degrau = mydata['x1']
    resp = mydata['y1']
    tempo = mydata['T']

    C = len(degrau)  # numero de colunas
    L = len(degrau)  # numero de linhas


    F = np.array([resp[0, 0:C-1], degrau[0, 0:C-1]],)
    F = F.T  # Matriz transposta
    print(F)

    J = np.array([resp[0, 1:C], ])
    print(J)
    J = J.T
    

    tempo = np.array([tempo[0, 0:C-1], ])
    # tempo = tempo.T

    C = len(tempo[0])
    L = len(tempo)
    # print("coluna ", C)
    # print("linha ", L)

    Theta = np.linalg.pinv(np.dot(F.T, F))
    Theta = np.dot(Theta, F.T)
    Theta = np.dot(Theta, Theta) 
    # Theta = [0.5, 0.75]
    print(Theta)

    # coeficientes
    a1 = Theta[0]
    b1 = Theta[1]
    
    # print(a1)
    # print(b1

    # funcao de transferencia Z
    #sysS = tf(b1, a1, 0.2)
    # sysZ = tf([b1], [1-a1], 0.2)
    # print(sysS)
    return Theta

# ----------------------------------Sistema-------------------------------------



Theta = minimos_quadrados()
a1 = Theta[0]
b1 = Theta[1]

Kp = 13  # Ganho proporcional
Ki = 0.5  # Ganho integral
Kd = 1  # Ganho derivativo


Ts = 0.2  # Tempo de amostragem
SP = 50  # Setpoint
PV = 0  # Precess Value

tempo2 = np.arange(0, 350, 0.2)[-1]

resposta_ma = malha_aberta(tempo2, a1, b1, PV, SP, Ts, tempo2)
resposta_mf = malha_fechada_sem_ganho(tempo2, a1, b1, PV, SP, Ts, tempo2)
resposta_mfc = malha_fechada_controlador_PID(
    tempo2, a1, b1, PV, SP, Kp, Ki, Kd, Ts, tempo2)

# Chamando os gráficos
# graficos(tempo2, resposta_ma, resposta_mf, resposta_mfc)
grafico(tempo2, resposta_mfc)


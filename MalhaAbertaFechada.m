%% Definindo as variaveis de entrada e saida
u=x1;%Degrau Aplicado
y=y1;%Resposta do Sistema de N�vel
%%Definindo o numero de amostras
x=size(u);
N=x(1);
M=N-1;
%% Definindo os tempos envolvidos
T=0.1; %Tempo de Amostragem
t=[0:T:M*T];
%%Criando a Matriz F e vetor Y
F=[y(1:M,1) u(1:M,1)];
Y=[y(2:N,1)];
%%Calculando os coeficientes a1 e b1
theta=inv(F'*F)*F'*Y;
a1=theta(1,1);
b1=theta(2,1);

%%Calculando a fun��o em Z

sysz=tf([b1],[1 -a1],T);

%%Calculando a fun��o em S

syss=d2c(sysz);
ye = step(u(1)*syss,t);

%MALHA FECHADA
syss_F=feedback(syss,1);
yef= step(40*syss_F,t);

plot(t,ye,'r',t,yef,'b')

%plot(t,ye)

%SAIDA MALHA FECHADA COM CONTROLADOR

%% Aplicando o algoritmo para verificar a sa�da do sistema em malha fechada com controlador PI
a1 = 0.9963;
b1 = 0.0070;
T = 0.1;
%Definindo pv como sendo a sa�da do sistema
pv(1)=0;
% Definindo cont como a sa�da do controlador PI
cont(1)=0;
%%Definindo a a��o proporcional do sitema
P(1)=0;
%%Definindo a a��o integral do sistema
I(1)=0;
sp=40;
%%Definindo o ganho proporcional do sistema
Kp=10.8952;
%%Definindo o ganho integral do sistema
Ki=2.8182;
M = 1600;
%%Implementando a malha fechada do sistema com controlador PI
%% Por meio da utiliza��o da equa��o a diferen�as do sistema
for i=2:1:M+1
  pv(i)=a1*pv(i-1)+b1*cont(i-1); %% Sa�da instantanea do sistema
  erro(i)=sp - pv(i); %% Erro instataneo do sistema
  P(i)=Kp*erro(i); %% A��o proporcioanl
  I(i)=I(i-1)+Ki*erro(i)*T; %A��o Integral
  cont(i)=P(i)+I(i); %%A��o do controlador PI saida
  t(i)=T*i; %%vari�vel de tempo
end
%%Plotando os gr�ficos de entrada e sa�da do sistema
plot(t,ye,'r',t,yef,'b',t,pv,'g')
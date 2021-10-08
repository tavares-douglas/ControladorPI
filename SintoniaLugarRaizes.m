Num = 1.89
Den = [26.99 1]
Mp = input('Digite o Valor do Máximo Pico em %: ' )
Ta = input('Digite o Valor do Tempo de Acomodação em [s]: ')
Ess = 0
%________________ Cálculo Ki_______________________
if (Ess ~=0) 
    Kv = 1/Ess;
    Ki = Kv/Num(1);   
else
    Kv = 0
end
%__________________________________________________
Mp1 = Mp/100; Mp2 = log(Mp1)/(-pi); 
Qsi = sqrt((Mp2^2)/(1+Mp2^2)) % Cálculo de Qsi
Wn = (4/(Qsi*Ta)) % Cálculo de Wn.
s1 = -Qsi*Wn + i*Wn*sqrt(1-Qsi^2);
abss1 = abs(s1); 
BETA = angle(s1)*(180/pi);
Gs1 = Num /((s1*Den(1)) + Den(2));
absGs1 = abs(Gs1);
PHI = (angle(Gs1)*180)/pi;
if (Ess ~= 0)  
    Kp = (-sind(BETA + PHI))/(absGs1*sind(BETA))-((2*Ki*cosd(BETA))/abss1);
    Kd = sind(PHI)/(abss1*absGs1*sind(BETA)) + (Ki/abss1^2);
else
    Ki = -((sind(PHI)/(abss1*absGs1*sind(BETA)))*abss1^2)
    Kp = (-sind(BETA + PHI))/(absGs1*sind(BETA))-((2*Ki*cosd(BETA))/abss1);
    Kd = 0;
end
Ki
Kp
Kd
C_s = tf([Kd Kp Ki],[1 0]);
sys = tf(Num,Den)
D = series(C_s,sys);
E = feedback(D,1);
step(E*40);
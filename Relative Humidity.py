import math

T1 = 10 #outside Temp
T2 = 20 #inside Temp
RH1 = 100 #outside relative humidity
RH2 = 0 #inside relative humidity
RH3 = 0 #

absMoisture1 = 0 #absolute moisture in the value that is calculated
absMoisture2  = 0#wanted absolute moisture
absMoisureTot = 0

absMoisture1 = (RH1 * 0.42 * math.exp(T1 * 10 * 0.006235398) / 10)
RH2 = (absMoisture1 * 10 / (0.42 * math.exp(T2 * 10 * 0.006235398)))

print(RH2)
valor_sal, hora_extra, bonif = input().split()

valor_sal = float(valor_sal)
hora_extra = int(hora_extra)
bonif = int(bonif)

hora_trabajo = valor_sal / 166
hora_extra = ((hora_trabajo * 0.37) + hora_trabajo) * hora_extra
total_bonif = (valor_sal * 0.095)*bonif

sal_net = valor_sal + hora_extra + total_bonif

salud = sal_net * 0.04
pension = sal_net * 0.03
caja = sal_net * 0.02

sal_tot = sal_net - salud - pension - caja

print(round(sal_net, 1), round(sal_tot, 1))
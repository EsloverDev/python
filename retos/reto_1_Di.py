Salario_Base, Hora_Extra, Bonificacion = input().split()

Salario_Base = float(Salario_Base) 
Hora_Extra = int(Hora_Extra)
Bonificacion = int(Bonificacion) 

Valor_Hora_Normal = Salario_Base/187
Valor_Horas_Extras = (Valor_Hora_Normal + Valor_Hora_Normal*0.39)*Hora_Extra

Total_Bonificacion = (Salario_Base*0.066)*Bonificacion

Salario_Total = Salario_Base + Valor_Horas_Extras + Total_Bonificacion

Desc_Salud = Salario_Total*0.05
Desc_Pension = Salario_Total*0.02
Desc_Caja_Comp = Salario_Total*0.01

Salario_Final = Salario_Total - Desc_Salud - Desc_Pension - Desc_Caja_Comp

print(round(Salario_Total, 1), round(Salario_Final, 1))
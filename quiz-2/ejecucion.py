# se solicita los datos al usuario
nombre = input("Por favor ingrese el nombre de trabajador: ")
dias_laborados = int(input("Por favor ingrese el número de días laborados en la empresa: "))
salario = float(input("Por favor ingrese el salario mensual del trabajador: "))

# se calculan valores
prima = salario * dias_laborados / 360
cesantias = salario * dias_laborados / 360
intereses_cesantias = cesantias * 0.12 / dias_laborados
vacaciones = salario * dias_laborados / 720
liquidacion_total = prima + cesantias + intereses_cesantias + vacaciones

# imprime resultados
print(f"\nSeñor {nombre} para los {dias_laborados} días laborados y")
print(f"salario ${salario:,.0f}, su liquidación se compone así:")
print(f"Prima: ${prima:,.2f}")
print(f"Cesantía: ${cesantias:,.2f}")
print(f"Intereses cesantías: ${intereses_cesantias:,.2f}")
print(f"Vacaciones: ${vacaciones:,.2f}")
print(f"Liquidación total: ${liquidacion_total:,.2f}")

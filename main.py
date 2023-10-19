# Clientes Classic:

#Tarjeta de débito.
#Caja de ahorro en pesos.
#Opcionalmente, caja de ahorro en dólares con cargo mensual.
#Hasta 5 retiros de dinero en efectivo sin comisiones, luego se aplica una tarifa. Límite diario de retiro de $10,000 por cajero.
#No tienen acceso a tarjetas de crédito.
#Comisión del 1% por transferencias salientes y 0.5% por transferencias entrantes.

#Clientes Gold:

#Tarjeta de débito.
#Hasta 2 cajas de ahorro y una cuenta corriente sin cargos adicionales. Se aplica un cargo mensual extra por cajas de ahorro en dólares adicionales.
#Tarjetas VISA y/o Mastercard con hasta 5 extensiones cada una, con límites de $150,000 en un pago y $100,000 en cuotas.
#Máximo de $20,000 en retiros diarios sin comisiones. Retiros ilimitados sin costo mensual.
#Acceso a cuentas de inversión.
#Posibilidad de tener una chequera.
#Comisión del 0.5% por transferencias salientes y 0.1% por transferencias entrantes.

#Clientes Black:

#Hasta 5 tarjetas de débito.
#Hasta 5 cajas de ahorro en pesos y dólares sin cargos adicionales, luego se aplica un cargo extra.
#Hasta 3 cuentas corrientes sin cargos adicionales.
#Tarjetas VISA, Mastercard y/o American Express con hasta 10 extensiones cada una, con límites de $500,000 en un pago y $600,000 en cuotas.
#Retiro máximo de $100,000 por día sin comisiones, con retiros ilimitados al mes sin costo adicional.
#Acceso a cuentas de inversión.
#Posibilidad de tener hasta dos chequeras.
#No se aplican comisiones a las transferencias.

import funciones

# Ejemplo 1
print(f"Total: {int(funciones.calcular_monto_total(1000,100,35,10))}")
# Ejemplo 2
print(f"Sin comision: {int(funciones.descontar_comision(1000,5))}")
# Ejemplo 3 
print(f"Total plazo fijo: {int(funciones.calcular_monto_plazo_fijo(100000,10))}")
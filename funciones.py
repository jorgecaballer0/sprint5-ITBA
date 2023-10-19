### FUNCIONES
# Compra de dolares con impuestos
def calcular_monto_total(precio_dolar, cantidad, impuesto_pais, ganancias):
    total_sin_impuestos = precio_dolar * cantidad
    impuestos = (total_sin_impuestos * impuesto_pais / 100) + (total_sin_impuestos * ganancias / 100)
    monto_total = total_sin_impuestos + impuestos
    return monto_total

# Comision
def descontar_comision(monto, comision):
    monto_comision = (monto * comision) / 100
    monto_descontado = monto - monto_comision
    return monto_descontado

# Plazo fijo
def calcular_monto_plazo_fijo(monto, tasa_interes):
    monto_final = monto * (1 + tasa_interes / 100)
    return monto_final

def calcular_descuento(cantidad,cliente):
    descuento = 0
    if cantidad >= 10_000 and cantidad <= 20_000:
        descuento = 0.1
    elif cantidad >= 20_001 and cantidad <= 40_000:
        descuento = 0.15
    elif cantidad > 40_000:
        descuento = 0.2

    if cliente == 'COMMAQ':
        descuento -= 0.02
    elif cliente == 'BEL':
        descuento += 0.01

    return descuento

# Entrenamiento por lotes

LIMITE_VRAM = 2500  # MB
total_cargado = 0
num_lote = 0

while True:
    mb = int(input("Tamaño del lote (MB): "))
    
    if total_cargado + mb > LIMITE_VRAM:
        print(f"ERROR OOM: {total_cargado + mb} MB supera el límite.")
        print("Carga detenida.")
        break
    
    total_cargado += mb
    num_lote += 1
    print(f"Lote #{num_lote} cargado. Total: {total_cargado} MB")
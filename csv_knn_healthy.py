import csv

# Ruta del archivo original y del nuevo archivo corregido
archivo_entrada = 'test/knn_houses_results_almost_final.csv'
archivo_salida = 'test/archivo_corregido.csv'

with open(archivo_entrada, 'r', newline='', encoding='utf-8') as infile, \
     open(archivo_salida, 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.DictReader(infile, delimiter=';')
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    for row in reader:
        valor_original = row['mean_test_score']
        
        # Sustituir coma por punto
        valor = valor_original.replace(',', '.')

        # Si empieza por un dígito sin punto decimal, añadir "0." delante
        if not valor.startswith('0.') and not valor.startswith('1.') and '.' in valor:
            parte_entera, parte_decimal = valor.split('.', 1)
            if parte_entera != '0':
                valor = f"0.{parte_entera}{parte_decimal}"

        # Reemplazar el valor en la fila
        row['mean_test_score'] = valor
        writer.writerow(row)

print(f"Archivo corregido guardado como: {archivo_salida}")
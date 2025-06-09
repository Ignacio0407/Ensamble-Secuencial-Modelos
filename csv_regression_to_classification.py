import pandas as pd
from pathlib import Path

csv_path = Path('csv/parkinsons.csv')
df = pd.read_csv(csv_path)

# 2. Verificar que la última columna es 'SalePrice'
last_column = df.columns[-1]

# 3. Calcular la mediana de 'SalePrice' (ignorar NaN)
median_value = df[last_column].median()

# 4. Convert lastColumn to 0 (low) o 1 (high) using the median as threshold
df[last_column] = (df[last_column] > median_value).astype(int)

# 5. Guardar el nuevo CSV
new_csv_path = csv_path.with_name(f"{csv_path.stem}_clasification{csv_path.suffix}")
df.to_csv(new_csv_path, index=False)

print(f"Nuevo archivo guardado en '{new_csv_path}'")
print(f"Mediana usada para clasificación: {median_value:.2f}")
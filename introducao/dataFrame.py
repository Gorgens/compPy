import pandas as pd
import numpy as np

outorgas = pd.read_csv('OutorgasFelicioDosSantos.csv', encoding='latin-1')
print(outorgas.shape)

for col in outorgas.columns:
    print(col)

print(outorgas['Vazao Jan'].head())
print(outorgas['Tipo'].unique())

print(outorgas.filter(items=['Tipo', 'Vazao Jan'])
    .groupby('Tipo')
    .sum())
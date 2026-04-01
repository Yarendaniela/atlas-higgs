import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta absoluta del CSV
file_path = r"C:\Users\Yaren Daniela\Desktop\atlas-higgs\data\atlas-higgs-challenge-2014-v2.csv"

# Cargar dataset
df = pd.read_csv(file_path)

# Crear carpeta plots si no existe
plots_dir = '../plots'
os.makedirs(plots_dir, exist_ok=True)

# Configuración de estilo
sns.set(style="whitegrid")

# Histograma de DER_mass_MMC
plt.figure(figsize=(10,6))
sns.histplot(df['DER_mass_MMC'], bins=50, kde=True, color='blue')
plt.title('Histograma de masa invariante (DER_mass_MMC)')
plt.xlabel('Masa invariante')
plt.ylabel('Frecuencia')
plt.savefig(os.path.join(plots_dir, 'mass_histogram.png'))
plt.show()

# Scatterplot de DER_pt_h vs DER_mass_MMC
plt.figure(figsize=(10,6))
sns.scatterplot(x=df['DER_pt_h'], y=df['DER_mass_MMC'], alpha=0.5)
plt.title('DER_pt_h vs DER_mass_MMC')
plt.xlabel('DER_pt_h')
plt.ylabel('DER_mass_MMC')
plt.savefig(os.path.join(plots_dir, 'pt_vs_mass.png'))
plt.show()
# Cargo las librerias 
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import sys
sys.path.append('/Users/SoapyGenie/Dropbox/Documentos/Estudios/Master IA/Minerí­a de datos y modelización predictiva')

# Establecemos nuestro escritorio de trabajo
os.chdir('/Users/SoapyGenie/Dropbox/Documentos/Estudios/Master IA/Minerí­a de datos y modelización predictiva/Datos')

# Cargo las funciones que voy a utilizar
from FuncionesMineria import (analizar_variables_categoricas, cuentaDistintos, frec_variables_num, atipicosAmissing, 
                               patron_perdidos, ImputacionCuant, ImputacionCuali)

# Cargo los datos
datos = pd.read_excel('DatosEleccionesEspaña.xlsx')

# Comprobamos el tipo de formato de las variables variable que se ha asignado en la lectura.
# No todas las categoricas estan como queremos
datos.dtypes

datos['Izquierda'] = datos['Izquierda'].astype(str)
datos['Derecha'] = datos['Derecha'].astype(str)
datos['AbstencionAlta'] = datos['AbstencionAlta'].astype(str)
datos['ActividadPpal'] = datos['ActividadPpal'].astype(str)
datos['Densidad'] = datos['Densidad'].astype(str)
datos['CCAA'] = datos['CCAA'].astype(str)
datos['CodigoProvincia'] = datos['CodigoProvincia'].astype(str)

variables = list(datos.columns)  
numericas = datos.select_dtypes(include=['int', 'int32', 'int64','float', 'float32', 'float64']).columns
categoricas = [variable for variable in variables if variable not in numericas]

frec_variables_num(datos, categoricas)
cuentaDistintos(datos)


# Muestra valores perdidos
datos[variables].isna().sum()



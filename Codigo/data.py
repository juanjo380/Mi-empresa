import pandas as pd 
import numpy as np
from os import path

def initiation(user):

    if not path.exists(f"./datos/{user}_pagos.csv"):
        df = pd.DataFrame({'ID':[], 'Nombre':[], 'Precio':[], 'Descripción': [], 'Unidades': []})
        df.to_csv(f"./datos/{user}_pagos.csv")            
            

def add_product(user, producto): #Producto debe ser una lista como: [nombre, precio, descripción, unidades]
    df = pd.read_csv(f"./datos/{user}_pagos.csv",index_col=0)

    if producto[0] in df['Nombre'].values:
        df.loc[df['Nombre'] == producto[0],'Unidades'] += int(producto[3])

    else:

        for i in range(250):
            Id = np.random.randint(300,400)
            if  Id not in df['ID']:
                break

        new_row = pd.DataFrame([[Id, producto[0], int(producto[1]), producto[2], int(producto[3])]], columns=df.columns)
        df = pd.concat([df,new_row], ignore_index=True)

    df.to_csv(f"./datos/{user}_pagos.csv") 
    
    return Id
import sqlite3
import pandas

               
        #Read xlsx file
raw_client_list = pandas.read_excel("Clientes.xlsx")
print(raw_client_list.columns)
        #Replace NaN values (empty cells for 0)
#raw_client_list['Unnamed: 0'].fillna(0, inplace=True)

        #Get only the columns that we need
clients = raw_client_list['CLIENTE'].values
zone = raw_client_list['ZONA'].values
time = raw_client_list['HORARIO'].values
user = raw_client_list['USUARIO'].values

        #Database connection
conn = sqlite3.connect('database/products_db.db')
        #Delete previous products
query = f"DELETE FROM Cliente"
cursor = conn.execute(query)

        #Auxiliary index
i = 0
    #Insert into database
for client in clients:
            #print(codes[i],product)
    query = f"INSERT INTO Cliente (Cliente,Zona,Horario,Usuario) VALUES ('{client}','{zone[i]}','{time[i]}',{user[i]})"

    try:
        cursor = conn.execute(query)
        conn.commit()
                    #products.append(product)
    except sqlite3.Error as er:
        print(er)
                             
    i += 1
        
print("TERMINO")
import json
import mysql.connector as sql_db 

def main():
    try:
        db = mysql()
        # insert(db)
        selectCliente(db)
        
        db.close()
        

    except Exception as e:
        print("Erro na aplicação  Arroz<Feijão=inverseParam", e)
def selectCliente(db):
    cursor = db.cursor()
    sql = 'SELECT nomeCliente, idade, sexo FROM cliente'
    
    cursor.execute(sql)

    listaCliente = []
    for (nomeCliente, idade, sexo) in cursor:        
        listaCliente.append({
            "nomeCliente": nomeCliente,
            "idade": idade,
            "sexo": sexo
        })
    
    # print(listaCliente)
    escrever_json(listaCliente)


def insert(db):
    data = ler_json('cliente.json')
    #dados do cliente
    nomeCliente = data['nomeCliente']
    idade = data['idade']
    sexo = data['sexo']
    #endereco do cliente
    rua = data['endereco']['rua']
    bairro = data['endereco']['bairro']
    numero = data['endereco']['numero']
    cidade = data['endereco']['cidade']
    uf = data['endereco']['uf']
    pais = data['endereco']['pais']        

    cursor = db.cursor()

    sql = 'INSERT INTO cliente (nomeCliente, idade, sexo) VALUES (%s, %s, %s)'

    values = [
        (nomeCliente, idade, sexo)
    ]

    cursor.executemany(sql, values)
    db.commit()

    print(cursor.rowcount, "Registros inseridos em clientes")

def mysql():
    database  = sql_db.connect(
        host="localhost",
        user="joao",
        password="joazin",
        database="cliente"
    )
    return database

def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as arquivo:
        return json.load(arquivo)

def escrever_json(lista):
    with open('clienteDB.json', 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo)        

if __name__ == "__main__":
    main()
    



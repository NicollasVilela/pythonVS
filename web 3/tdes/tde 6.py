import mysql.connector

conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                passwd = '',
                database = 'tde6'
                )
x = conexao.cursor()

x.execute('create database tde6')

x.execute(
CREATE TABLE IF NOT EXISTS Cliente (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('Pessoa Física', 'Pessoa Jurídica')),
    endereco TEXT,
    telefone TEXT,
    cpf TEXT UNIQUE,
    cnpj TEXT UNIQUE
)
)

x.execute(
CREATE TABLE IF NOT EXISTS Editora (
    id_editora INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT,
    telefone TEXT,
    gerente TEXT
)
)

x.execute(
CREATE TABLE IF NOT EXISTS Livro (
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    autor TEXT,
    assunto TEXT,
    editora_id INTEGER,
    isbn TEXT UNIQUE,
    quantidade_estoque INTEGER,
    FOREIGN KEY (editora_id) REFERENCES Editora(id_editora)
)
)

x.execute(
CREATE TABLE IF NOT EXISTS Compra (
    id_compra INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    livro_id INTEGER,
    data_compra TEXT,
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id_cliente),
    FOREIGN KEY (livro_id) REFERENCES Livro(id_livro)
)
)

conexao.commit()

x.execute("INSERT INTO Cliente (nome, tipo, endereco, telefone, cpf) VALUES ('João Silva', 'Pessoa Física',\
    'Rua A, 123', '123456789', '123.456.789-00')")

x.execute("INSERT INTO Editora (nome, endereco, telefone, gerente) VALUES ('Editora XYZ', 'Rua B, 456',\
    '987654321', 'Maria')")
          

x.execute("INSERT INTO Livro (titulo, autor, assunto, editora_id, isbn, quantidade_estoque) VALUES 'Livro A', 'Autor A', 'Assunto A', 1,\
    '978-3-16-148410-0', 10)")

conexao.commit()

x.execute("SELECT * FROM Cliente")
clientes = x.fetchall()
print(clientes)

x.execute("SELECT id_cliente FROM Cliente")
codigos_clientes = x.fetchall()
print(codigos_clientes)

x.execute("SELECT titulo, quantidade_estoque FROM Livro")
estoque_livros = x.fetchall()
print(estoque_livros)

x.execute("UPDATE Cliente SET nome = ? WHERE id_cliente = ?", ('João da Silva', 1))
conexao.commit()



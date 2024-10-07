# import mysql.connector

# conexao = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd=''
# )

# x = conexao.cursor()

# x.execute('CREATE DATABASE tde6')
# x.execute('USE tde6')

# x.execute('''
# CREATE TABLE Cliente (
#     id_cliente INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(255) NOT NULL,
#     tipo ENUM('Pessoa Física', 'Pessoa Jurídica'),
#     endereco VARCHAR(255),
#     telefone VARCHAR(20),
#     cpf VARCHAR(14) UNIQUE,
#     cnpj VARCHAR(18) UNIQUE
# )
# ''')

# x.execute('''
# CREATE TABLE Editora (
#     id_editora INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(255) NOT NULL,
#     endereco VARCHAR(255),
#     telefone VARCHAR(20),
#     gerente VARCHAR(255)
# )
# ''')

# x.execute('''
# CREATE TABLE Livro (
#     id_livro INT AUTO_INCREMENT PRIMARY KEY,
#     titulo VARCHAR(255) NOT NULL,
#     autor VARCHAR(255),
#     assunto VARCHAR(255),
#     editora_id INT,
#     isbn VARCHAR(20) UNIQUE,
#     quantidade_estoque INT,
#     FOREIGN KEY (editora_id) REFERENCES Editora(id_editora)
# )
# ''')

# x.execute('''
# CREATE TABLE Compra (
#     id_compra INT AUTO_INCREMENT PRIMARY KEY,
#     cliente_id INT,
#     livro_id INT,
#     data_compra DATE,
#     FOREIGN KEY (cliente_id) REFERENCES Cliente(id_cliente),
#     FOREIGN KEY (livro_id) REFERENCES Livro(id_livro)
# )
# ''')

# conexao.commit()

# x.execute("INSERT INTO Cliente (nome, tipo, endereco, telefone, cpf) VALUES ('João Silva', 'Pessoa Física', 'Rua A, 123', '123456789', '123.456.789-00')")
# x.execute("INSERT INTO Editora (nome, endereco, telefone, gerente) VALUES ('Editora XYZ', 'Rua B, 456', '987654321', 'Maria')")
# x.execute("INSERT INTO Livro (titulo, autor, assunto, editora_id, isbn, quantidade_estoque) VALUES ('Livro A', 'Autor A', 'Assunto A', 1, '978-3-16-148410-0', 10)")

# conexao.commit()

# x.execute("SELECT * FROM Cliente")
# clientes = x.fetchall()
# print(clientes)

# x.execute("SELECT id_cliente FROM Cliente")
# codigos_clientes = x.fetchall()
# print(codigos_clientes)

# x.execute("SELECT titulo, quantidade_estoque FROM Livro")
# estoque_livros = x.fetchall()
# print(estoque_livros)

# x.execute("UPDATE Cliente SET nome = %s WHERE id_cliente = %s", ('João da Silva', 1))
# conexao.commit()

# conexao.close()


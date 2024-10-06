import mysql.connector

conexao = mysql.connector.connect(
                host = 'localhost',
                user = 'root',
                passwd = '',
                database = 'aula9'
                )
x = conexao.cursor()
#print(conexao)

'''x.execute('create database aula9')
#mostrar todas as bases de dados -----------------------------------------------

x.execute('show databases')
for a in x:
    print(a)

#criar tabela ------------------------------------------------------------------

x.execute('create table aluno(matricula int(10) primary key AUTO_INCREMENT,\
nome varchar(30) not null, idade int(3),email varchar(50))')

#mostrar todas as tabelas -----------------------------------------------------

x.execute('show tables')
for b in x:
    print(b)

#descrever a tabela ----------------------------------------------------------
x.execute('describe aluno')
for c in x:
    print(c)
    
#Inserir valores insert into nome da tabela (atributos) values (valores) --------

x.execute('insert into aluno(nome,idade,email) values ("Thereza",23,"exemplo@gmail.com")')
conexao.commit()

print(x.rowcount,'registro(s) inserido(s)')

#inserir multiplos valores ------------------------------------------------------

y= 'insert into aluno(nome,idade,email) values (%s,%s,%s)'
val = [
    ('Maria','12','exemplo1@gmail.com'),
    ('Jose', '32', 'exemplo2@gmail.com'),
    ('Mariana', '2', 'exemplo3@gmail.com'),
    ('Manuela', '52', 'exemplo4@gmail.com'),
    ('Paula', '42', 'exemplo5@gmail.com'),
    ('Mario', '78', 'exemplo6@gmail.com'),
    ('Eva', '82', 'exemplo7@gmail.com'),
]
x.executemany(y,val)
conexao.commit()
print(x.rowcount,'registro(s) inserido(s)')

#select -----------------------------------------------------------------

x.execute('select * from aluno')
result = x.fetchall()
print(result)

for i in result:
    print(i)
    
#------------------------------------------------------------------------

x.execute('select nome,idade from aluno')
result1 = x.fetchall()
print(result1)

for i in result1:
    print(i)
# select com condição - where() -----------------------------------------------

x.execute('select nome, idade from aluno where idade > 20')
result2 = x.fetchall()
print(result2)

for i in result2:
    print(i)

# drop() - apaga tudooooooooooooooooooo ----------------------------------------

x.execute('drop database agencia')
x.execute('drop table nome da tabela')

# delete - para deletar registros -----------------------------------------------

x.execute('delete from aluno where matricula = 4')
conexao.commit()
print(x.rowcount,'Registros deletados')

#deletar varios registros -------------------------------------------------------

s = 'delete from aluno where matricula in (%s,%s)'
x.execute(s,(3,8))
conexao.commit()
print(x.rowcount,'Registros deletados')

#between() - deleta entre intervalos ------------------------------------------

s = 'delete from aluno where matricula  between %s and %s'
x.execute(s,(5,7))
conexao.commit()
print(x.rowcount,'Registros deletados')

#-----------------------------------------------------------------------------
y= 'insert into aluno(nome,idade,email) values (%s,%s,%s)'
val = [
    ('Maria','12','exemplo1@gmail.com'),
    ('Jose', '32', 'exemplo2@gmail.com'),
    ('Mariana', '2', 'exemplo3@gmail.com'),
    ('Manuela', '52', 'exemplo4@gmail.com'),
    ('Paula', '42', 'exemplo5@gmail.com'),
    ('Mario', '78', 'exemplo6@gmail.com'),
    ('Eva', '82', 'exemplo7@gmail.com'),
]
x.executemany(y,val)
conexao.commit()

#order by() -------------------------------------------------------------

x.execute('select nome from aluno order by nome')
res = x.fetchall()
for i in res:
    print(i)
#----------------------------------------------------------------------

x.execute('select nome from aluno order by nome desc ')
res1 = x.fetchall()
for i in res1:
    print(i)
    
#update() - atualizar tabela ------------------------------------------

x.execute('update aluno set nome ="Thereza Gondim" where matricula =1')
conexao.commit()
print(x.rowcount,'Registro(s) atualizado(s)')

#alter table() - alterar tabela adicionando nova coluna ----------------------------------

x.execute('alter table aluno add endereco varchar(100)')
conexao.commit()

#trocar nome da coluna -----------------------------------------------------------

x.execute('alter table aluno change column endereco teste varchar(50)')
conexao.commit()'''

#renomear o nome da tabela -----------------------------------------------------

x.execute('alter table aluno rename pessoa')
conexao.commit()
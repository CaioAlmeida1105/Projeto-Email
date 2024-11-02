#IMPORTANDO BIBLIOTECAS
import imaplib as il
from  datetime import datetime
import email
from email.utils import parsedate_to_datetime

#COLETANDO INFORMAÇÕES
usuario = str(input("Informe seu endereço de E-mail:"))
senha = str(input("Informe sua senha:"))
servidor = str(input("Informe seu servidor (ex: imap.gmail.com):"))
pasta = str(input("Informe a pasta do seu E-mail que você deseja selecionar:"))

#LOGANDO NO SERVIDOR
meu_email = il.IMAP4_SSL(servidor)
meu_email.login(usuario, senha)


#SELECIONANDO A PASTA NO MODO LEITURA
meu_email.select(pasta, readonly=True)

#BUSCANDO E-MAILS NÃO LIDOS
status, emails = meu_email.search(None, 'UNSEEN')
if status == 'OK':
    email_ids = emails[0].split()
    print(f"Total de e-mails não lidos na pasta '{pasta}': {len(email_ids)}")
else:
    print("Não foi possível acessar a pasta.")

#DESCOBRINDO QUE HORAS O E-MAIL FOI MANDADO
for num in email_ids:
    #RECUPERANDO E-MAIL PELO ID
    status, data_email = meu_email.fetch(num, '(RFC822)')

    #OBTENDO O CONTEUDO DO E-MAIL
    mensagem = email.message_from_bytes(data_email[0][1])

    #EXTRAINDO A DATA DO CABEÇALHO
    data_envio = mensagem['Date']

    #CONVERTENDO A DATA PARA HORARIO
    hora = parsedate_to_datetime(data_envio).strftime('%H:%M')

    #EXIBINDO AS INFORMAÇÕES
    print(f'ID: {num.decode()} | Horário de envio: {hora} ')

#LOGOUT DO E-MAIL
meu_email.logout()


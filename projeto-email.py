#IMPORTANDO BIBLIOTECAS
import imap_tools as it
import imaplib as il

#COLETANDO INFORMAÇÕES
usuario = str(input("Informe seu endereço de E-mail:"))
senha = str(input("Informe sua senha:"))
servidor = str(input("Informe seu servidor (ex: imap.gmail.com):"))
pasta = str(input("Informe a pasta do seu E-mail que você deseja selecionar:"))
meu_email = il.IMAP4_SSL(servidor)

#FUNÇÃO DE LOGAR AO SERVIDOR
def logar():
    meu_email.login(usuario, senha)
    return meu_email

#FUNÇÃO DE CONTAR E-MAILS NÃO LIDOS
def contando_emails():
    meu_email.select(pasta)
    status, emails = meu_email.search(None, 'UNSEEN')
    if status == 'OK':
        email_ids = emails[0].split()
        print(f"Total de e-mails não lidos na pasta '{pasta}': {len(email_ids)}")
    else:
        print("Não foi possível acessar a pasta.")

#APLICANDO FUNÇÕES
logar()
contando_emails()

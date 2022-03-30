from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import APIKey #A chave


with open('login.txt','r') as aux:
  User_Email = aux.readlines() #Lendo email do arquivo

user = User_Email[0]




#Infomando dados (De, Para, Título, Mensagem de duas formas)
Message = Mail(from_email=user,to_emails='pessoa@gmail.com', subject='Enviando Meu Primeiro Email com Python', plain_text_content='Hello Word! 2',html_content='Hello Word!')

try:
  sg = SendGridAPIClient(APIKey.Key)#Autenticando a chave  
  response = sg.send(Message)#Enviando Email
  print("Email enviado")

except:
  print("Erro ao enviar email. Verificar código.")

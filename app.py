from flask import Flask, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.json

    # Obtener los datos del formulario
    name = data.get('name')
    email = data.get('email')
    date = data.get('date')

    # Enviar correo electrónico
    sender_email = 'tucorreo@gmail.com'  # Cambia esto por tu dirección de correo
    receiver_email = 'destinatario@gmail.com'  # Cambia esto por la dirección del destinatario
    password = 'tucontraseña'  # Cambia esto por tu contraseña

    message = MIMEMultipart("alternative")
    message["Subject"] = "Nuevo formulario enviado"
    message["From"] = sender_email
    message["To"] = receiver_email
   
    text = f"""
    Nombre: {name}
    Email: {email}
    Fecha: {date}
    """

    part1 = MIMEText(text, "plain")
    message.attach(part1)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    return jsonify({'message': 'Formulario enviado correctamente'})

if __name__ == '__main__':
    app.run(debug=True)

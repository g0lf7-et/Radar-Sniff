import numpy as np
import matplotlib.pyplot as plt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fonction pour scanner les fréquences
def scan_frequency_range():
    frequencies = np.linspace(100, 1000, 100)
    print("Scanning frequencies...")
    for freq in frequencies:
        print(f"Detected signal at {freq} MHz")
        # Condition pour déclencher l'alerte (par exemple, fréquence > 900 MHz)
        if freq > 900:
            send_alert(freq)  # Envoie une alerte si la fréquence est supérieure à 900 MHz
    return frequencies

# Fonction pour envoyer une alerte 
def send_alert(freq):
    # Configuration de l'email 
    sender_email = "ton.email@example.com"
    receiver_email = "ton.email@example.com"  # Changez avec l'email du destinataire
    password = "tonMotDePasse"  
    
    # Création du message
    subject = f"Alerte : Fréquence suspecte détectée ({freq} MHz)"
    body = f"Les ondes radio des forces de l'ordre ont été détectées à {freq} MHz."

    # Créer le message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Envoi de l'email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"Alerte envoyée pour {freq} MHz !")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'alerte : {e}")

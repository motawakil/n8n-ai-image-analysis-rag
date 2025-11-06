  # Python script to send images


# Exemple en Python
import requests
import base64

# Lire et encoder l'image
with open('image-produit.jpeg', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

# Envoyer à n8n
webhook_url = "http://localhost:5678/webhook-test/fcc2d240-4220-410d-b11b-94909452455b"
payload = {
    "image": encoded_image,
    "filename": "image-produit.jpeg",
    "mimeType": "image/jpeg"
}

response = requests.post(webhook_url, json=payload)
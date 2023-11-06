from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# NO SE USA AL FINAL

# Cargar la clave privada
with open('api_public_key.pem', 'rb') as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

    
def verify_signature(signature, message):
    # Verificar la firma con la clave pública
    print(signature)
    print(message)
    print(public_key)
    message_bytes = message.encode('utf-8')
    print(message_bytes)
    try:
        public_key.verify(
            signature,
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True  # La firma es válida
    except InvalidSignature:
        return False  # La firma no es válida
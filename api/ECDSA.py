import hashlib
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey
from ellipticcurve.signature import Signature

from flask import Flask

# Genera una clave privada para un usuario
def genKeys():
    privateKey = PrivateKey()
    # Generamos una clave publica p
    publicKey = privateKey.publicKey()
    return(privateKey.toString(), publicKey.toString())

# Generamos una firma 
# Requiere la clave privada del usuario que firma y el contenido del archivo
# a firmar
def genSignature(userprivatekey, file):
    # Genera un digest del archivo usando SHA256
    message = hashlib.sha256(file).hexdigest()

    # Generamos la firma del documento usando el digest y la clave privada
    signature = Ecdsa.sign(message, PrivateKey.fromString(userprivatekey))

    # Devuelve la firma y la clave publica del documento
    return signature._toString()

def fileVerify(file, sign, publickey):
    # Generamos un digest del documento a verificar
    message = hashlib.sha256(file).hexdigest()
    
    isSignatureEquals = Ecdsa.verify(message, Signature._fromString(sign), PublicKey.fromString(publickey))
    
    return isSignatureEquals
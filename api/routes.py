from flask import Blueprint, request
from . import ECDSA as ec
import os

blueprint = Blueprint(
    'api',
    __name__,
    url_prefix='/eSignatureApi/v1'
)

@blueprint.get('/generateKey')
def generateKey():
    keys = ec.genKeys()
    result = {'private_key': keys[0], 'public_key': keys[1]}
    return result

@blueprint.get('/verify')
def verifyFile():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../tmp/test')

    signature = request.form['signature']
    public_key = request.form['public_key']
    file = request.files['file']
    file.save(filename)
    
    with open (filename, 'rb') as input_file:
        message = input_file.read()

    os.remove(filename)

    result = {'result': ec.fileVerify(message, signature, public_key) }

    return result

@blueprint.get('/generateSignature')
def generateSignature():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../tmp/test')

    private_key = request.form['private_key']
    file = request.files['file']
    file.save(filename)

    with open (filename, 'rb') as input_file:
        message = input_file.read()

    os.remove(filename)

    signature = ec.genSignature(private_key, message)

    return signature
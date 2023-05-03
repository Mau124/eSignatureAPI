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
    key = 'asdf'
    return key

@blueprint.post('/generateSignature')
def generateSignature():
    # key = request.form['keys']
    # file = request.form['file']
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../tmp/test')

    data = request.files
    data2 = request.form
    print(data)
    print(data2)
    file = data['file']
    file.save(filename)
    print(file)

    key = ec.genKeys()

    ifile = open(filename, 'rb')
    input_file = ifile.read()
    print(input_file)
    print(key)
    signature = ec.genSignature(key[0], input_file)
    ifile.close()

    # print(key)
    # print(file)

    return signature
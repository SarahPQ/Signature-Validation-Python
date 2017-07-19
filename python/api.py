#!/usr/bin/env python

from hashlib import sha256
from base64 import b64encode


def generate_signature(signature):
    """
    Encodes a signature

    In Python 2.7+, it will return a String object whereas in Python 3 it
    will return a Bytes object

    +info: https://dev.payconiq.com/online-payments-dock/#signature

    :param signature: your key as string
    :return: string
    """
    shasum = sha256()
    shasum.update(signature.encode('utf-8'))
    signature_encoded = b64encode(shasum.digest())
    return signature_encoded

#!/usr/bin/env python

from hashlib import sha256
from base64 import b64encode


def generate_signature(merchant_id, currency, amount, secret_key, webhook_id=''):
    """
    Generates a signature according to Payconiq's algorithm

    In Python 2.7+, it will return a String object whereas in Python 3 it
    will return a Bytes object

    Please note that the order of the parameters in the signature must follow
    accordingly.

    +info: https://dev.payconiq.com/online-payments-dock/#signature

    :param merchant_id: string
    :param currency: string
    :param amount: string
    :param secret_key: string
    :param webhook_id: string. (optional). Defaults to empty string
    :return: string
    """
    shasum = sha256()
    signature = '{merchat_id}{webhook_id}{currency}{amount}{secret_key}'.format(
                                                    merchat_id=merchant_id,
                                                    webhook_id=webhook_id,
                                                    currency=currency,
                                                    amount=amount,
                                                    secret_key=secret_key)
    shasum.update(signature.encode('utf-8'))
    signature_encoded = b64encode(shasum.digest())
    return signature_encoded

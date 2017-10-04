# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CertificatePropertiesWithNonce(Model):
    """The description of an X509 CA Certificate including the challenge nonce
    issued for the Proof-Of-Possession flow.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar subject: The certificate's subject name.
    :vartype subject: str
    :ivar expiry: The certificate's expiration date and time.
    :vartype expiry: datetime
    :ivar thumbprint: The certificate's thumbprint.
    :vartype thumbprint: str
    :ivar is_verified: Determines whether certificate has been verified.
    :vartype is_verified: bool
    :ivar created: The certificate's create date and time.
    :vartype created: datetime
    :ivar updated: The certificate's last update date and time.
    :vartype updated: datetime
    :ivar verification_code: The certificate's verification code that will be
     used for proof of possession.
    :vartype verification_code: str
    """

    _validation = {
        'subject': {'readonly': True},
        'expiry': {'readonly': True},
        'thumbprint': {'readonly': True},
        'is_verified': {'readonly': True},
        'created': {'readonly': True},
        'updated': {'readonly': True},
        'verification_code': {'readonly': True},
    }

    _attribute_map = {
        'subject': {'key': 'subject', 'type': 'str'},
        'expiry': {'key': 'expiry', 'type': 'rfc-1123'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'is_verified': {'key': 'isVerified', 'type': 'bool'},
        'created': {'key': 'created', 'type': 'rfc-1123'},
        'updated': {'key': 'updated', 'type': 'rfc-1123'},
        'verification_code': {'key': 'verificationCode', 'type': 'str'},
    }

    def __init__(self):
        self.subject = None
        self.expiry = None
        self.thumbprint = None
        self.is_verified = None
        self.created = None
        self.updated = None
        self.verification_code = None

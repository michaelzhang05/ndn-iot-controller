from ndn.encoding import TlvModel, BytesField, TypeNumber

TLV_SEC_BOOT_ANCHOR_DIGEST = 161
TLV_SEC_BOOT_CAPABILITIES = 160
TLV_AC_ECDH_PUB_N1 = 162
TLV_AC_ECDH_PUB_N2 = 163
TLV_AC_SALT = 131
TLV_AC_AES_IV = 135
TLV_AC_ENCRYPTED_PAYLOAD = 136
TLV_POLICY_DATA_STR = 140
TLV_POLICY_KEY_STR = 141
TLV_SSP_DEVICE_CAPABILITIES = 143

# Security Sign On protocol
class SignOnRequest(TlvModel):
    identifier = BytesField(TypeNumber.GENERIC_NAME_COMPONENT)
    capabilities = BytesField(TLV_SEC_BOOT_CAPABILITIES)
    ecdh_n1 = BytesField(TLV_AC_ECDH_PUB_N1)


class SignOnResponse(TlvModel):
    anchor = BytesField(TypeNumber.DATA)
    ecdh_n2 = BytesField(TLV_AC_ECDH_PUB_N2)
    salt = BytesField(TLV_AC_SALT)


class CertRequest(TlvModel):
    identifier = BytesField(TypeNumber.GENERIC_NAME_COMPONENT)
    ecdh_n2 = BytesField(TLV_AC_ECDH_PUB_N2)
    anchor_digest = BytesField(TLV_SEC_BOOT_ANCHOR_DIGEST)
    ecdh_n1 = BytesField(TLV_AC_ECDH_PUB_N1)
    capabilities = BytesField(TLV_SSP_DEVICE_CAPABILITIES)

class CertResponse(TlvModel):
    id_cert = BytesField(TypeNumber.DATA)
    iv = BytesField(TLV_AC_AES_IV)
    cipher = BytesField(TLV_AC_ENCRYPTED_PAYLOAD)


class PolicyAddRequest(TlvModel):
    data_name = BytesField(TLV_POLICY_DATA_STR)
    key_name = BytesField(TLV_POLICY_KEY_STR)


# Access Control protocol
class CipherBlock(TlvModel):
    iv = BytesField(TLV_AC_AES_IV)
    cipher = BytesField(TLV_AC_ENCRYPTED_PAYLOAD)

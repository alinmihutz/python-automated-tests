import base64


class Authentication(object):
    def __init__(
        self,
        enc,
        access_token,
        token_type,
        expires_in,
        autologin_url
    ):
        self.type = token_type
        self.expires_in = expires_in
        self.enc = enc
        self.token = access_token

        session_data = base64.b64decode(access_token).decode('utf-8')
        self.session_id = session_data[(session_data.index('-') + 2)::]
        self.autologin_url = autologin_url

    def get_autologin_url(self):
        return self.autologin_url

    def get_enc(self):
        return self.enc

    def get_token(self):
        return self.token

    def get_type(self):
        return self.type

    def get_session_id(self):
        return self.session_id

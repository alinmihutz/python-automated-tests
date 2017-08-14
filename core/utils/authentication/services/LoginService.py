import json
import urllib.error
import urllib.parse
import urllib.request

from core.utils.authentication.services.Authentication import Authentication
from core.utils.authentication.services.Login import Login
from core.utils.authentication.services.LoginFailedException import LoginFailedException


class LoginService(object):
    __autologin_secure_url = 'https://secure.meetic.com/authent/secure.php?autoLogonEnc={{enc}}&host={{host}}'
    __authent_route = 'https://{{preHost}}authent.ilius.net{{postHost}}/oauth/accesstokens'

    def verify_credentials(self, login: Login):
        authent_url = str(self.__authent_route)\
            .replace('{{preHost}}', login.get_env().preHost)\
            .replace('{{postHost}}', login.get_env().postHost)

        request_header = {'Authorization': 'Basic VU5MLk1FRS5GUjo=', 'content-type': 'application/json'}
        request_body = {'grant_type': 'password', 'username': login.get_email(), 'password': login.get_password()}

        request = urllib.request.Request(
            authent_url,
            data=json.dumps(request_body).encode('utf8'),
            headers=request_header
        )

        try:
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            raise LoginFailedException('Authent failed with ' + str(e.code) + ' ' + str(e.msg))
        except urllib.error.URLError as e:
            raise LoginFailedException('Authent failed with URLError ' + str(e.reason))
        else:
            # 200 OK
            decoded_response = json.loads(response.read().decode('UTF-8'))

            autologin_url = str(self.__autologin_secure_url)\
                .replace('{{enc}}', decoded_response['enc'])\
                .replace('{{host}}', login.get_host())

            enc = decoded_response['enc']
            access_token = decoded_response['access_token']
            token_type = decoded_response['token_type']
            expires_in = decoded_response['expires_in']

            return Authentication(
                decoded_response['enc'],
                decoded_response['access_token'],
                decoded_response['token_type'],
                decoded_response['expires_in'],
                autologin_url
            )

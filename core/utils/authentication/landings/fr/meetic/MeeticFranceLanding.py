from core.utils.authentication.landings.AventadorLanding import AventadorLanding
from core.utils.user.User import User


class MeeticFranceLanding(AventadorLanding):
    _show_loginform_css_selector = "div[class='show-loginform already-member']"
    _show_loginform_link_text = "Déjà membre ?"

    def login(self, user: User):
        AventadorLanding.login(self, user)

    def registration(self):
        pass

    def pre_login(self):
        self._show_loginform_or_raise_error()

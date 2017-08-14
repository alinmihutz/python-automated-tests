from core.utils.authentication.landings.AventadorLanding import AventadorLanding


class MeeticSpainLanding(AventadorLanding):
    _show_loginform_css_selector = "div[class='show-loginform already-member']"
    _show_loginform_link_text = "Inicia sesión"

    def registration(self):
        pass

    def pre_login(self):
        self._show_loginform_or_raise_error()


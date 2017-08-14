from core.utils.authentication.components.FormLoginComponent import FormLoginComponent


class WebDriverLoginComponent(FormLoginComponent):
    def input_email_address(self, email):
        self.email_input_web_element.send_keys(email)

    def input_password(self, password):
        self.password_input_web_element.send_keys(password)

    def submit_login_form(self):
        self.submit_form_web_element.click()

    def check_remember_me_checkbox(self, check_remember_me=FormLoginComponent.REMEMBER_ME):
        is_checked = self.remember_me_web_element.get_attribute('checked')

        if check_remember_me and not is_checked:
            self.remember_me_web_element.click()
        elif not check_remember_me:
            if is_checked:
                self.remember_me_web_element.click()
        else:
            pass

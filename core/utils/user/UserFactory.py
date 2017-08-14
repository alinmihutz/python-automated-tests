from core.utils.user.User import User
from core.utils.user.UserNotFoundException import UserNotFoundException


class UserFactory(object):
    man_looking_for_woman = 'HF'
    woman_looking_for_man = 'FH'

    @staticmethod
    def create_user(email_address, password, brand) -> User:
        return User(email_address, password, brand)

    def create_woman_looking_for_man_user(self, users_external_resources):
        if self.woman_looking_for_man in users_external_resources:
            return User(
                users_external_resources[self.woman_looking_for_man][0],
                users_external_resources[self.woman_looking_for_man][1],
                users_external_resources[self.woman_looking_for_man][2],
            )

        raise UserNotFoundException({
            'error': {
                'context': self.__class__,
                'problem': 'User not found exception !',
                'solution': ''
            }
        })

    def create_man_looking_for_woman_user(self, users_external_resources):
        if self.man_looking_for_woman in users_external_resources:
            return User(
                users_external_resources[self.man_looking_for_woman][0],
                users_external_resources[self.man_looking_for_woman][1],
                users_external_resources[self.man_looking_for_woman][2],
            )

        raise UserNotFoundException({
            'error': {
                'context': self.__class__,
                'problem': 'User not found exception !',
                'solution': ''
            }
        })

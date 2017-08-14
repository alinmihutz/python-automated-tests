from core.utils.authentication.landings.es.meetic.MeeticSpainLanding import MeeticSpainLanding
from core.utils.authentication.landings.fr.meetic.MeeticFranceLanding import MeeticFranceLanding
from core.utils.authentication.landings.uk.match.MatchUKLanding import MatchUKLanding


class LandingFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def create_landing(web_driver, domain, brand):
        if 'meetic.fr' == brand + '.' + domain:
            return MeeticFranceLanding(web_driver)
        if 'meetic.es' == brand + '.' + domain:
            return MeeticSpainLanding(web_driver)
        if 'uk.match' == domain + '.' + brand:
            return MatchUKLanding()

        return None

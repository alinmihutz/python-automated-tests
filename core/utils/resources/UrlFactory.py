class UrlFactory(object):
    @staticmethod
    def construct_url(pre_host, host, post_host):
        url = "https://"
        url += pre_host
        url += host
        url += post_host

        return url

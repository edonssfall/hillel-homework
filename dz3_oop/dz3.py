

class Url:

    def __init__(self, scheme = str(), authority = str(), path = list(), query = dict(), fragment = list()):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, object):
        return str(self) == str(object)

    def __str__(self):
        text = str()
        if len(self.scheme) > 0:
            text += f"{self.scheme}://"
        if len(self.authority) > 0:
            text += self.authority
        if len(self.path) > 0:
            for pathes in self.path:
                text += f"/{pathes}"
            self.path.clear()
        if len(self.query) > 0:
            text += "?"
            for key,value in self.query.items():
                text += f"{key}={value}&"
            text = text[:-1]
            self.query.clear()
        if len(self.fragment) > 0:
            text += "#"
            for fragments in self.fragment:
                text += f"{fragments}"
        return text

class HttpUrl(Url):

    def __init__(self, scheme="http", authority=str(), path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class HttpsUrl(Url):

    def __init__(self, scheme="https", authority=str(), path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class GoogleUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="google.com", path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class WikiUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="wikipedia.org", path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

class UrlCreator(Url):
    path_list = []
    def __init__(self, scheme=str(), authority=str(), path=list(), query=dict(), fragment=list()):
        super().__init__(scheme, authority, path, query, fragment)

    def _create(self):
        return str(self)

    def __call__(self, *args, **kwds):
        for arg in args:
            self.path.append(arg)
        for key, value in kwds.items():
            self.query.update({key: value})
        return UrlCreator(self.scheme, self.authority, self.path, self.query)
            
    def __getattr__(self, name):
        self.path.append(name)
        return UrlCreator(self.scheme, self.authority, self.path)




class Url:

    def __init__(self, scheme="", authority="", path=[], query={}, fragment=[]):
        self.scheme = scheme
        self.authority = authority
        self.path = path
        self.query = query
        self.fragment = fragment

    def __eq__(self, object):
        return str(self) == str(object)

    def __str__(self):
        text = ""
        if len(self.scheme) > 0:
            text += f"{self.scheme}://"
        if len(self.authority) > 0:
            text += self.authority
        if len(self.path) > 0:
            for pathes in self.path:
                text += f"/{pathes}"
        if len(self.query) > 0:
            text += "?"
            for key,value in self.query.items():
                text += f"{key}={value}&"
            text = text[:-1]
        if len(self.fragment) > 0:
            text += "#"
            for fragments in self.fragment:
                text += f"{fragments}"
        return text

class HttpUrl(Url):

    def __init__(self, scheme="http", authority="", path=[], query={}, fragment=""):
        super().__init__(scheme, authority, path, query, fragment)

class HttpsUrl(Url):

    def __init__(self, scheme="https", authority="", path=[], query={}, fragment=""):
        super().__init__(scheme, authority, path, query, fragment)

class GoogleUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="google.com", path=[], query={}, fragment=""):
        super().__init__(scheme, authority, path, query, fragment)

class WikiUrl(HttpsUrl):

    def __init__(self, scheme="https", authority="wikipedia.org", path=[], query={}, fragment=""):
        super().__init__(scheme, authority, path, query, fragment)

class UrlCreator(Url):

    def __init__(self, scheme="", authority="", path=[], query={}, fragment=[]):
        super().__init__(scheme, authority, path, query, fragment)

    def _create(self):
        return Url.__str__(self)

    def __call__(self, *args, **kwds):
        for arg in args:
            self.path.append(arg)
        for key, value in kwds.items():
            self.query.update({key: value})
        print(self.path, "query")
        return UrlCreator(self.scheme, self.authority)

            
    def __getattr__(self, name):
        path_list = []
        path_list.append(name)
        return UrlCreator(self.scheme, self.authority, path=path_list)


url_creator = UrlCreator(scheme='https', authority='docs.python.org')
print(url_creator.docs.v1.api.list)
print(url_creator.docs.v1.api.list)
print(url_creator.path)
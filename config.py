DEBUG=True

ADMIN=frozenset(['name@example.com'])

CSRF_ENABLED=True
CSRF_SESSION="somethingimpossibletoguess"
SECRET_KEY='bupt-zhengnan'

OPENID_PROVIDERS = [
    {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
    {'name':'Yahoo','url':'https://me.yahoo.com'},
    {'name':'AOL','url':'http://openid.aol.com/<username>'},
    {'name':'Flickr', 'url':'http://www.flickr.com/<username>'},
]

__export__ = ['get_acl', 'keys_for']

def __authorized_keys(metadata):
    return metadata.Properties['authorized_keys.xml'].XMLMatch(metadata)

def __members_in_acl(keys, acl):
    return keys.findall('/AuthorizedKeys/ACL[@name="%s"]/Member/text()' % acl)

def __keys_for_user(keys, user):
    return keys.findall('/AuthorizedKeys/User[@name="%s"]/Key/text()' % user)

def get_acl(metadata, acl):
    keys = __authorized_keys(metadata)
    return __members_in_acl(keys, acl)

def keys_for(metadata, acl):
    keys = __authorized_keys(metadata)
    users = __members_in_acl(keys, acl)
    return [key for user in users for key in __keys_for_user(keys, user)]

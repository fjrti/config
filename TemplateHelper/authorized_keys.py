__export__ = ['get_acl', 'keys_for']

def __authorized_keys(metadata):
    return metadata.Properties['authorized_keys.xml'].XMLMatch(metadata)

def __members_in_acl(keys, acl):
    members = keys.findall('.//ACL[@name="%s"]/Member' % acl)
    return map(lambda x: x.text, members)

def __keys_for_user(keys, user):
    return keys.findall('.//User[@name="%s"]/Key' % user)

def get_acl(metadata, acl):
    keys = __authorized_keys(metadata)
    return __members_in_acl(keys, acl)

def keys_for(metadata, acl):
    keys = __authorized_keys(metadata)
    users = __members_in_acl(keys, acl)

    out = []
    for user in users:
        for key in __keys_for_user(keys, user):
            key_type = key.get('type', 'ssh-rsa')
            comment = '%s@%s' % (user, key.get('host', 'unknown'))
            out.append(' '.join([key_type, key.text, comment]))
    return out

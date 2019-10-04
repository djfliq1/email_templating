

def create_login(fname, lname):
    login = lname[:4] + fname[:2]
    return login


def create_password(fname, lname):
    password = fname[:3] + lname[:3] + '12345'
    return password

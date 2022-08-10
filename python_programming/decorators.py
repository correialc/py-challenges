'''Bla'''

def extended_get_msg(f):
    '''Bla'''
    def inner_func(*args, **kwargs):
        '''Bla'''
        msg = f(*args, **kwargs)
        print("You have a new message")
        return msg
    return inner_func

@extended_get_msg
def get_msg(dest_name):
    '''Bla'''
    return f"Message to {dest_name}"

print(get_msg("Joe"))

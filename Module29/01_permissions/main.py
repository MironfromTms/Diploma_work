import functools

user_permissions = ['admin']


def check_permission(name):
    def wrap_fun(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            try:
                if name in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print('PermissionError: This user can not add comment')

        return wrapped_func

    return wrap_fun


@check_permission('admin')
def delete_site():
    print('Delete the site')


@check_permission('user_1')
def add_comment():
    print('Add comment')


delete_site()
add_comment()

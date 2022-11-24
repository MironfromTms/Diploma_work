from contextlib import contextmanager

user_permissions = ['admin']


def check_permission(name):
    def wrap_fun(func):
        def wrapped_func(*args, **kwargs):
            if name == 'admin':
                func(*args, **kwargs)
            else:
                print('PermissionError: This user can not add comment')

        return wrapped_func

    return wrap_fun


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

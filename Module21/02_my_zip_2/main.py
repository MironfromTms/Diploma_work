# TODO здесь писать код
def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in args) for i in range(length)]
    return tpl_list

# TODO здесь писать код
def shortes_range(string, tpl):
    return min(len(string), len(tpl))


syms_str = 'abcd'
nums_tpl = (10, 20, 30, 40)

pairs = ((syms_str[i_elem], nums_tpl[i_elem]) for i_elem in range(shortes_range(syms_str, nums_tpl)))
print(pairs)
for i in pairs:
    print(i)
def my_zip(*args):
    length = min(len(element) for element in args)
    tpl_list = [tuple(struct[i] for struct in args) for i in range(length)]
    return tpl_list

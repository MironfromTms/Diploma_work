# TODO здесь писать код
def check_registration_info(first_list, second_list):
    with open('registrations_good.log:', 'a') as good_reg_list:
        for j_line in first_list:
            good_reg_list.write(j_line + '\n')
    with open('registrations_bad.log:', 'a') as bad_reg_list:
        for n_line in second_list:
            bad_reg_list.write(n_line + '\n')


with open('registrations.txt', 'r', encoding='utf8') as reg_file:
    good_list = []
    bad_list = []
    for line in reg_file:
        line = line[:-1]
        split_line = line.split(' ')
        try:
            if len(split_line) == 3:
                if split_line[0].isalpha():
                    if split_line[0].isalpha():
                        if '@' in split_line[1] and '.' in split_line[1]:
                            if split_line[2].isdigit and 10 <= int(split_line[2]) <= 99:
                                good_list.append(line)
                            else:
                                raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99: ')
                        else:
                            raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку):')
                    else:
                        raise NameError('Поле «Имя» содержит НЕ только буквы')
                else:
                    raise NameError('Поле «Имя» содержит НЕ только буквы')

            else:
                raise IndexError('НЕ присутствуют все три поля')
        except (IndexError, NameError, SyntaxError, ValueError) as exc:
            print(exc)
            bad_list.append(line)

    check_registration_info(good_list, bad_list)

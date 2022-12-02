import re

phones_list = ['9999999999', '999999-999', '99999x9999']
good_phone_numbers_list = []
pattern = r'[8:9]\d{9}'
for i_number in phones_list:
    good_phone_numbers = re.findall(pattern, i_number)
    good_phone_numbers_list.append(good_phone_numbers)
for j_number in phones_list:
    if j_number in good_phone_numbers_list[0]:
        print(j_number, ':is correct phone number')
    else:
        print(j_number, ':is wrong phone number')


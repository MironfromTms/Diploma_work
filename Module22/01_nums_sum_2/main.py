# TODO здесь писать код
numbers_file = open('numbers.txt', 'r')
summ_of_numbers = []
for i_number in numbers_file:
    info = i_number.split()
    summ_of_numbers.append(info)
    summ_of_numbers_list = [i for y in summ_of_numbers for i in y]
int_summ = 0
for i in summ_of_numbers_list:
    int_summ += int(i)
answer = open('answer.txt', 'w')
answer.write(str(int_summ))

print('Содержимое файла answer.txt')
print(int_summ)
numbers_file.close()
answer.close()
# TODO здесь писать код
def is_polindrome(num_list):
    reversed_list = []
    for i_num in range(len(num_list)-1,-1,-1):
        reversed_list.append(num_list[i_num])
    if num_list == reversed_list:
        return True
    else:
        return False

nums = int(input('Кол-во чисел: '))
nums_list = []
new_nums = []
answer = []
for i in range(nums):
    print('Введите', i + 1, ' число : ', end='')
    element = int(input())
    nums_list.append(element)

for i_nums in range(0, len(nums_list)):
    for j_elem in range(i_nums, len(nums_list)):
        new_nums.append(nums_list[j_elem])
    if is_polindrome(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums_list[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Последовательность: ', nums_list)
print('Нужно приписать чисел: ', len(answer))
print('Сами числа:', answer)
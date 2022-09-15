zen_text = open('zen.txt', 'r', encoding='utf8')
zen_text_list = []
for i_str in zen_text:
    zen_text_list.append(i_str)
for i_str in zen_text_list[::-1]:
    print(i_str, end='')

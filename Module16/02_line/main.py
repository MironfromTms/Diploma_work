# TODO здесь писать код
first_class = []
for i in range(160, 177, 2):
    first_class.append(i)

print(first_class)

secound_class = []

for i in range(162, 181, 3):
    secound_class.append(i)

print(secound_class)

new_class = first_class+secound_class
new_class.sort()
print(new_class)

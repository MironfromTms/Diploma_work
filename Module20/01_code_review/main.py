students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_and_len_surnames(dictionary):
    interests = list()
    len_of_surnames = str()
    for i in dictionary:
        interests += (dictionary[i]['interests'])
        len_of_surnames += dictionary[i]['surname']
    counter = 0
    for _ in len_of_surnames:
        counter += 1
    return interests, counter


id_and_ages = list()
for i_id in students:
    id_and_ages.append((i_id, students[i_id]['age']))
print('Список пар "ID студента - Возраст": ', id_and_ages)


answer = interests_and_len_surnames(students)[0]
surnames_len = interests_and_len_surnames(students)[1]

print('Полный список интересов всех студентов: ', answer)
print('Общая длина всех фамилий студентов:', surnames_len)

# TODO исправить код

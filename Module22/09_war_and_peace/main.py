# TODO здесь писать код
import collections
import zipfile


def unzip(archive):
    z_file = zipfile.ZipFile(archive, 'r')
    for i_file_name in z_file.namelist():
        z_file.extract(i_file_name)
    z_file.close()


def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[0:-3], 'txt'))
    text_file = open('voyna-i-mir.txt', 'r', encoding='utf8')
    for i_line in text_file:
        for i_letter in i_line:
            if i_letter.isalpha():
                if i_letter not in result:
                    result[i_letter] = 0
                else:
                    result[i_letter] += 1
    text_file.close()

    return result


def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{: ^9}|{: ^9}|".format("Буква", " Частота"))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{: ^9}|{: ^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_values in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_values:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict


file_name = 'voyna-i-mir.txt'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)

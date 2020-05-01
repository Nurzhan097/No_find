#!/usr/bin/python
import io

# НАхождение похожего слова в списке
def find_word(word, list_s):
    for item in list_s:
        if word in item:
            return True
    return False


def find_line(word_find, file_name):
    word = word_find
    print(ord(word))
    print('search in file word: "', word,'"')
    with io.open(file_name, encoding='utf-8') as file:
        f = open('orders_'+file_name, 'w')
        list_to_file = []
        for line in file:
            if word in line:
                #print(line, end=' ')
                strip_line = line.split(' ')
                for word_index in range(len(strip_line)):
                    word_in_line = strip_line[word_index]
                    if word in word_in_line and '	' not in word_in_line:
                        if len(word_in_line) <= 1 :
                            word_to_list = word_in_line + strip_line[word_index+1]
                        else:
                            word_to_list = word_in_line
                        #print(word_to_list)
                        # append to list
                        if '\n' in word_to_list:
                            word_to_list = word_to_list[:len(word_to_list)-2]
                        if not find_word(word_to_list, list_to_file):
                            list_to_file.append(word_to_list)
                            print(word_to_list)
        print(list_to_file)                
        for item in list_to_file:
            f.write(item + '\n')
                # print(strip_line)
        

print("<== START PROGRAM by Nurzhan ==>")
print('Hi, Aibar! Wish you a good day!')
file_name = input("Введите название файла: ")
find_line("№", file_name)

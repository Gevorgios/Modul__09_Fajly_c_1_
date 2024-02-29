# with open('file1.txt', 'w') as file1:
#     file1.write("Hello, this is file 1\n")
#     file1.write("This is line 2\n")
#     file1.write("This is line 3\n")
#
# with open('file2.txt', 'w') as file2:
#     file2.write("Hello, this is file 2\n")
#     file2.write("This is line 2\n")
#     file2.write("This is line 3\n")
#
#
# def compare_files(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         lines1 = f1.readlines()
#         lines2 = f2.readlines()
#
#         for line1, line2 in zip(lines1, lines2):
#             if line1.strip() != line2.strip():
#                 print(f"Несовпадающая строка из файла 1: {line1.strip()}")
#                 print(f"Несовпадающая строка из файла 2: {line2.strip()}")
#                 break
#         else:
#             print("Файлы совпадают")
#
# # Пример использования функции
# compare_files("file1.txt", "file2.txt")


# 2


# def create_input_file():
#     with open("input.txt", 'w') as file:
#         file.write("Пример текста для анализа: \n")
#         file.write("Этот текст содержит 25 символов.\n")
#         file.write("И занимает 3 строки.\n")
#         file.write("В нем 10 гласных букв и 15 согласных.\n")
#         file.write("Также в тексте есть 5 цифр.\n")
#
# def get_statistics(input_file, output_file):
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     digits = "0123456789"
#
#     with open(input_file, 'r') as file:
#         content = file.read()
#         char_count = len(content)
#         lines = content.split('\n')
#         line_count = len(lines)
#         vowel_count = sum(1 for char in content if char in vowels)
#         consonant_count = sum(1 for char in content if char in consonants)
#         digit_count = sum(1 for char in content if char in digits)
#
#     with open(output_file, 'w') as file:
#         file.write(f"Количество символов: {char_count}\n")
#         file.write(f"Количество строк: {line_count}\n")
#         file.write(f"Количество гласных букв: {vowel_count}\n")
#         file.write(f"Количество согласных букв: {consonant_count}\n")
#         file.write(f"Количество цифр: {digit_count}\n")
#
#
# # Создаем файл input.txt
# create_input_file()
#
# # Пример использования функции
# get_statistics("input.txt", "output.txt")


# 3


# def create_input_file():
#     with open("input.txt", 'w') as file:
#         file.write("Это первая строка в файле\n")
#         file.write("Это вторая строка в файле\n")
#         file.write("Это третья строка в файле\n")
#
# def remove_last_line(input_file, output_file):
#     with open(input_file, 'r') as file:
#         lines = file.readlines()
#
#     with open(output_file, 'w') as file:
#         file.writelines(lines[:-1])
#
#
# create_input_file()

# remove_last_line("input.txt", "output.txt")



# 4


# def create_example_file(file_name):
#     lines = [
#         "Это первая строка в файле",
#         "Это вторая строка в файле",
#         "А вот это третья строка, самая длинная да короче"
#     ]
#
#     with open(file_name, 'w') as file:
#         for line in lines:
#             file.write(line +  "\n")
#
#
# def find_longest_line_length(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             lines = file.readline()
#             longest_line_length = max(len(line.strip()) for line in lines)
#             return longest_line_length
#     except FileNotFoundError:
#         print(f"Файл {file_name} не найден")
#         return -1
#
# file_name = "example.txt"
# create_example_file(file_name)
# longest_line_length = find_longest_line_length(file_name)
# if longest_line_length != -1:
#     print(f"Длина самой длинной строки в файле {file_name} составляет {longest_line_length} символов")



# 5



# def count_word_occurrences(file_name, target_word):
#     try:
#         with open(file_name, 'r') as file:
#             text = file.read()
#             word_count = text.lower().count(target_word.lower())
#             return word_count
#     except FileNotFoundError:
#         print(f"Файл {file_name} не найден")
#         return -1
#
#
# file_name = "example.txt"
# target_word = "строка"
#
# word_occurrences = count_word_occurrences(file_name, target_word)
# if word_occurrences != -1:
#     print(f"Слово {target_word} встречается в файле {file_name} {word_occurrences} раз")


# def replace_word_in_file(file_name, target_word, replacement_word):
#     try:
#         with open(file_name, 'r') as file:
#             text = file.read()
#             modified_text = text.replace(target_word, replacement_word)
#         with open(file_name, 'w') as file:
#             file.write(modified_text)
#
#         print(f"Слово {target_word} было заменено на {replacement_word} в файле {file_name}")
#     except FileNotFoundError:
#         print(f"Файл {file_name} не найден")
#
# file_name = "example.txt"
# target_word = "старое_слово"
# replacement_word = "новое_слово"
#
# replace_word_in_file(file_name, target_word, replacement_word)
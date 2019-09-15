# Вывести последнюю букву в слове
import re

word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(re.findall('а', word.lower())))

number_a = 0
for letter in word.lower():
    if letter == 'а':
        number_a += 1
print(number_a)

# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len(re.findall('[аоиеёэыуюя]', word.lower())))

number_a = 0
for letter in word.lower():
    if letter in 'аоиеёэыуюя':
        number_a += 1
print(number_a)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# можно ли тут lambda функцию?
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# можно ли писать в одну строку?
common_len = 0
words_list = sentence.split(' ')
for word in words_list:
    common_len += len(word)
print(int(common_len/len(words_list)))
import re

text = input()

# Разбив текста на слова удаление пунктуации, кроме цифр и букв
words = re.findall(r'\b[a-zA-Za-яА-Я0-9]+\b', text)

#Подсчёт слов с хотя бы двумя одинаковыми буквами
count_same_letters = 0
for word in words:
    # Убрать цифры
    letters_only = ''.join([char for char in word if char.isalpha()])
    # Проверяем, есть ли повторяющиеся буквы
    if len(letters_only) != len(set(letters_only)):
        count_same_letters += 1

#Вывод слов с ровно одной цифрой, удаляя арифметические знаки
arithmetic_signs = set('+-*/=')
words_with_one_digit = []

for word in words:
    # Счет количества цифр в слове
    digit_count = sum(1 for char in word if char.isdigit())
    # Проверка что цифра ровно одна
    if digit_count == 1:
        # Удаление арифметических знаков
        cleaned_word = ''.join([char for char in word if char not in arithmetic_signs])
        words_with_one_digit.append(cleaned_word)
print(f"Количество слов с хотя бы двумя одинаковыми буквами: {count_same_letters}")
print("Слова с ровно одной цифрой (арифметические знаки удалены):")
for word in words_with_one_digit:
    print(word)

# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1:])



# Вывести количество букв а в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels_sum = 0
for letter in word:
    if  letter in "а, А, е":
        vowels_sum = vowels_sum + 1
print("vowels_sum =", vowels_sum)
    

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
letters = [word[0] for word in words]
print("".join(letters))


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
average = sum(len(word) for word in words) / len(words)
print(average)
song = list(map(str, input("Введите текст песни, в которой фразы через пробел, а слова через тире").split()))
print(song)

def number(text):
    vowels = set("уеоаыию")
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count


if number(song[0]) == number(song[1]) == number(song[2]):
    print("Парам пам-пам")
else: print('Пам парам')


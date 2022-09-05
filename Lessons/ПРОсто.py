morze_dict = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
              'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
              'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
              'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya' , 'П': 'p'}


def Cleaner(func):
    def wrapper(s):
        if "--" in func(s):
            while func(s).count('--'):
                s = func(s).replace('--', '-')
                st = str(s).strip("-")
            return st
        else:
            return func(s)

    return wrapper


@Cleaner
def interpreter(text):
    translation = []

    for letter in text:
        if letter in ": ;.,_":
            translation.append('-')
        elif letter in morze_dict:
            translation.append(morze_dict[letter.lower()])
        else:
            translation.append(letter.lower())
    return "".join(translation)


s = input()

print(interpreter(s))
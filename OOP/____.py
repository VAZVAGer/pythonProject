from string import ascii_lowercase, digits
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" + ascii_lowercase
CHARS_CORRECT = CHARS + CHARS.upper() + digits
print(CHARS_CORRECT)

import  re

def dddd(number):
    pattern = r"\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d"
    match = re.fullmatch(pattern, number)
    print(True if match else False)

dddd("7777-0000-5650-2333")
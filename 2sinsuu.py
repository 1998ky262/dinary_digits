num = input()
def henkan (e):
    a = e
    s = ""
    while 0<a:
        s = str(a%2)+s
        a = a//2
    return s
result = henkan(num)
print(result)
#San loc so nguyen to
#is_prime[i] = True neu i la so nguyen to

LIMIT = 1_000_000
is_prime = [False, False] + [True] * (LIMIT - 1)
i = 2
while i * i <= LIMIT:
    if is_prime[i]:
        for j in range(i * i, LIMIT + 1, i):
            is_prime[j] = False
    i += 1

# bang xoay 180
STANDARD = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
EXTENDED = {**STANDARD, '2': '2', '5': '5'}

#kiem tra strobogrammatic
#xoay 180 do = dao chuoi * mang tung chu so -> phai ra chinh no
def is_strobo(n, ext=False):
    s = str(n)
    mp = EXTENDED if ext else STANDARD
    left, right = 0, len(s) - 1
    while left <= right:
        if s[left] not in mp or mp[s[left]] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# lay anh xoay 180
def rotate_image(n):
    s = str(n)
    result = ''
    for c in reversed(s):
        if c not in STANDARD:
            return None
        result += STANDARD[c]
    return None if result[0] == '0' else int(result)


print("a. So strobogrammatic < 1,000,000")
a = [n for n in range(1, LIMIT) if is_strobo(n)]
print(f"   Co {len(a)} so:", a, "\n")

print("b. Số nguyen to strobogrammatic < 1,000,000")
b = [n for n in a if is_prime[n]]
print(f"   Co {len(b)} so:", b, "\n")

print("c. So strobogrammatic mo rong < 1,000,000")
c = [n for n in range(1, LIMIT) if is_strobo(n, ext=True)]
print(f"   Co {len(c)} so:", c, "\n")

print("d. So nguyen to strobogrammatic mo rong < 1,000,000")
d = [n for n in c if is_prime[n]]
print(f"   Co {len(d)} so:", d, "\n")

print("e. Khong phai strobo, khong phai so nguyen to, nhung anh xoay la so nguyen to")
e = []
for n in range(2, LIMIT):
    if is_strobo(n): continue  # loai: da la strobo
    if is_prime[n]: continue  # loai: la so nguyen to
    img = rotate_image(n)
    if img and 2 <= img < LIMIT and is_prime[img]:
        e.append(n)
print(f"   Co {len(e)} so:", e[:50], "...")
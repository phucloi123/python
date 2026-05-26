def decode_cipher(cipher):
    result = ""
    i = 0
    while i < len(cipher):
        if cipher[i] == '#':
            count = int(cipher[i + 1])   # chữ số ngay sau # là số lần lặp
            char = cipher[i + 2]        # ký tự tiếp theo là ký tự được lặp
            result += char * count
            i += 3
        else:
            result += cipher[i]
            i += 1
    return result

# Test
print(decode_cipher("XY#6Z1#4023"))
print(decode_cipher("#39+1=1#30"))
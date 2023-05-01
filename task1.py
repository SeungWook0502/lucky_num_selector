input_data = input('Enter the code')

caesar_cipher = []

for i in input_data:
    if i in ['x','y','z','X','Y','Z']:
        caesar_cipher.append(chr(ord(i)-23))
    elif ord(i) in range(ord('A'), ord('x')): 
        caesar_cipher.append(chr(ord(i)+3))
    else:
        caesar_cipher.append('None')

print(''.join([i for i in caesar_cipher]))

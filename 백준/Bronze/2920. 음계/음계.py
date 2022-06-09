play = str(input()).replace(' ', '')
if play == '12345678':
    print('ascending')
elif play == '87654321':
    print('descending')
else:
    print('mixed')
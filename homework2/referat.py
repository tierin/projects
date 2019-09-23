

with open('referat.txt', 'r', encoding='utf-8') as ref, open('referat2.txt', 'w', encoding='utf-8') as ref2:
    referat = ref.read()
    len_ref = len(referat)
    print(len_ref)
    words_count = len(referat.split(' '))
    print(words_count)
    referat2 = referat.replace('.', '!')
    ref2.write(referat2)
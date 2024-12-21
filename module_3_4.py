def single_root_words(root_word, *other_words):
    same_words = []
    other_words = list(map(lambda x: x.lower(), other_words))
    root_word = root_word.lower()
    for i in range(len(other_words)):
        if other_words[i].count(root_word):
            same_words.append(other_words[i])
        if root_word.count(other_words[i]):
            same_words.append(other_words[i])
    return same_words
print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))


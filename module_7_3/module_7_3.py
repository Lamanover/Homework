import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf=8') as file:
                text = file.read().lower()
                text = text.translate(str.maketrans('', '', string.punctuation + '-'))
                words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}
        all_woeds = self.get_all_words()

        for file_name, words in all_woeds.items():
            if word in words:
                positions[file_name] = words.index(word) + 1

        return positions

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)

        return counts

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))


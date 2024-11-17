import string
result = string.punctuation
class WordsFinder:
    def __init__(self, *file):
        self.file = file

    def get_all_words(self):
        all_words = {}
        for filename in self.file:
            text1 = ''
            with open(filename, encoding='utf-8') as file1:
                for line in file1:
                    text = line.lower()
                    for i in result:
                        text = text.replace(i,'')
                    text = text.replace('\n', ' ')
                    text1 += text
                text2 = text1.split(' ')
                all_words[filename] = text2
        return all_words

    def find(self, word):
        slovarik = self.get_all_words().items()
        for name, words in slovarik:
            slovar = {}
            for i in range(0, len(words)+1):
                if  word.lower() == words[i]:
                    slovar[name] = i+1
                    return slovar


    def count(self, word):
        slovarik = self.get_all_words().items()
        for name, words in slovarik:
            slovar = {}
            kol = words.count(word.lower())
            slovar[name] = kol
            return slovar

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
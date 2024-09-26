import re


class WordsFinder:
    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for j in file:
                    j = j .lower()
                    j = re.sub(r'[,.=!?;:-]', '', j)
                    words.extend(j.split())
                    all_words[i] = words
        return all_words

    def find(self, word):
        result = {}
        index = 1
        for name, words in self.get_all_words().items():
            for i in words:
                if i.lower() == word.lower():
                    result[name] = index
                index += 1
        return result

    def count(self, word):
        result = {}
        index = 1
        for name, words in self.get_all_words().items():
            for i in words:
                if i.lower() == word.lower():
                    result[name] = index
                    index += 1
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

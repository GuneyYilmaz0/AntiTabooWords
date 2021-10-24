import yaml

import yaml_database

class Game:
    def __init__(self, gamemode):
        if gamemode == 1:
            self.easy_mode()

    def easy_mode(self):
        easy_file_path = "Easy.yml"
        data = yaml_database.yaml_loader(filepath=easy_file_path)
        words_data = data.get('Words')

    def check_answer(self, word1, answer, gamemode):
        if word1 != answer:
            print("Yanlış tahmin ettin. Tekrar dene\n")
            new_answer = input()
            self.check_answer(word1, new_answer, gamemode)



if __name__ == "__main__":
    Game(int(input("Bir oyun zorluk seviyesi seç: 1, 2, 3\n")))

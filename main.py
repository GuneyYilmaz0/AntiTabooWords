import random

import MainWindow
import yaml_database

taboo_history = {}


def is_cached(idx):
    if taboo_history.get(idx):
        return True
    else:
        taboo_history[idx] = 1
        return False


def yaml(mode):
    easy_file_path = f"{mode}.yml"
    words_data = yaml_database.yaml_loader(filepath=easy_file_path).get("Words")

    return words_data


def selecting(gamemode: int):
    if gamemode == 1:
        return select_word(gamemode="Easy")
    elif gamemode == 2:
        return select_word(gamemode="Normal")
    elif gamemode == 3:
        return select_word(gamemode="Hard")


def select_word(gamemode):
    words_data = yaml(gamemode)

    number = random.randint(0, len(words_data) - 1)
    if not is_cached(words_data[number]):
        return play(words_data[number])
    else:
        print("aynı kelime bulundu başka kelime verilecek")
        return select_word(gamemode)


def play(selected_word):
    return selected_word.split(":")


class Game:
    a = -1

    def __init__(self, gamemode):
        print("a")

    def normal_mode(self):
        words_data = yaml("Normal")
        selected_word = words_data[random.randint(0, len(words_data))]
        selected_word = selected_word.split(":")
        print("Kelimeyi tahmin et!\nYardımcı Kelimeler:" + selected_word[1] + ", " + selected_word[2])
        answer = input()
        self.check_answer(selected_word[0], answer, 2)

    def hard_mode(self):
        words_data = yaml("Hard")
        selected_word = words_data[random.randint(0, len(words_data))]
        selected_word = selected_word.split(":")
        print("Kelimeyi tahmin et!\nYardımcı Kelimeler:" + selected_word[1] + ", " + selected_word[2])
        answer = input()
        self.check_answer(selected_word[0], answer, 3)

    def check_answer(self, word1, answer, gamemode):
        if word1 != answer:
            print("Yanlış tahmin ettin. Tekrar dene\n")
            new_answer = input()
            self.check_answer(word1, new_answer, gamemode)

        print("Doğru bildin! +1 Puan")
        if gamemode == 1:
            self.select_word("Easy")


if __name__ == "__main__":
    MainWindow.setup()

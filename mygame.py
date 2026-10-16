import random

HIDDEN = '\u25A0'

WORDS = {
    'олень':    'Лесное рогатое животное',
    'тигр':     'Полосатый хищник из семейства кошачьих',
    'пингвин':  'Нелетающая птица, живёт в Антарктиде',
    'жираф':    'Самое высокое животное на Земле',
    'крокодил': 'Зелёная зубастая рептилия из тропиков',
    'медведь':  'Крупный хищник, любит мёд и малину',
    'лиса':     'Рыжая хитрюга из русских сказок',
    'волк':     'Серый хищник, живёт стаями',
    'сова':     'Ночная птица с большими глазами',
    'черепаха': 'Медлительное животное в панцире',
    'дельфин':  'Умное морское млекопитающее',
    'кенгуру':  'Прыгающее сумчатое из Австралии',
    'ёж':       'Колючий зверёк, сворачивается в клубок',
    'белка':    'Пушистый зверёк, запасает орехи',
    'слон':     'Огромное животное с хоботом',
}

def create_table(word, lives):
  return '\u25A0 ' * len(word) + ' | '
def is_alive(lives):
  return lives > 0
def show_table(table):
  print(table)
def prompt():
  return input()
def is_word_correct(word, answer):
  return word == answer
def show_message(msg):
  print(msg)
def dec_lives(lives):
  return lives - 1
def is_letter_correct(word, answer):
  return answer in word
def change_table(word, table, answer, lives):
  table = list(table)
  if answer in word:
    if word.index(answer) == 0:
      table[word.index(answer)] = answer
    else:
      table[word.index(answer) * 2] = answer
  table = ''.join(table)
  return table
def is_final_letter(word, letter):
  return len(word) == letter
def letter_inc(letter):
  return letter + 1
def show_gallows(lives):
  match lives:
    case 2:
      with open('gallows1.txt', 'r', encoding="utf-8") as f:
        print(f.read())
    case 1:
      with open('gallows2.txt', 'r', encoding="utf-8") as f:
        print(f.read())
    case 0:
      with open('gallows3.txt', 'r', encoding="utf-8") as f:
        print(f.read())
def show_hint(word):
  print(WORDS[word])

rnd = random.randrange(len(WORDS))
opened_letters = 0
keys = list(WORDS.keys())
current_word = keys[rnd]
lives = 3
table = create_table(current_word, lives)
msg_on_win = 'Вы выиграли! приз в студию!'
msg_on_ans = 'Назовите букву или слово целиком'
msg_on_fault = 'Неправильно. Вы теряете жизнь'
msg_on_lose = 'У вас закончились жизни! Вы проиграли!'

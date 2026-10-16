from mygame import *

while is_alive(lives):
    show_table(table)
    show_message(msg_on_ans)
    show_hint(current_word)
    answer = prompt()
    if is_word_correct(current_word, answer):
        show_message(msg_on_win)
        break
    elif is_letter_correct(current_word, answer):
        table = change_table(current_word, table, answer, lives)
        opened_letters = letter_inc(opened_letters)
        if is_final_letter(current_word, opened_letters):
          show_table(table)
          show_message(msg_on_win)
          break
    elif not is_letter_correct(current_word, answer):
        show_message(msg_on_fault)
        lives = dec_lives(lives)
        table = change_table(current_word, table, answer, lives)
        show_gallows(lives)
if not is_alive(lives):
  show_message(msg_on_lose)

import random

# 1 -> GLOBAL VARIABLES - required in the proposed solution
ideas_list ={}
idea_status = True
# 2 -> GRAPHICS
geme_titele = (
    """
                                                                                          
            ###  ########   #########  #########                ########
           ###  ###   ###  #########  #########                #########
          ###  ###   ###  ###        ###   ###                 ##   ###
         ###  ###   ###  ###        ###   ###                     ### 
        ###  ###   ###  ######     ###   ###                    ###
       ###  ###   ###  ######     #########                    ###
      ###  ###   ###  ###        #########                     ###
     ###  ###   ###  ###        ###   ###                      
    ###  ###   ###  #########  ###   ###                       ###
   ###  ########   #########  ###   ###                        ### 
    created by Paulina & Arek
    """
)
# 3 -> FUNCTIONS

def idea_append():
    global ideas_list
    idea_counter = len(ideas_list) + 1
    with open("ideas_bank.txt", "a", encoding='utf8') as f: 
        idea_text = input('What is your new idea?  ').capitalize()
        idea_key = str(idea_counter)
        f.write(f'{idea_key} | {idea_text}\n')
        idea_counter += 1


def idea_list():
    global ideas_list
    with open("ideas_bank.txt", "r", encoding='utf8') as f: 
        idea_list_append = f.readlines()                                            # czytanie zawartości pliku w postaci linii
        for line in idea_list_append:                                               # czytanie linia po lini
            line_clean = line.strip("\n").split(" | ")                              # formatowanie - otwarte pliki kończą się zawsze zapisem kończącym linie "/n", którego trzeba się pozbyć, dodatkowo zamieniam wartości ;lini na 2 zmienne pozbywając się widoczengo separatora " | "
            idea_list_key = str(line_clean[0])                                      # pobranie wartości pierwszej zmiennej z linii  klucz 
            idea_list_text = line_clean[1]                                          # pobranie wartości drugiej zmiennej z linii  text idei
            ideas_list[idea_list_key] = idea_list_text


def idea_print():
    for i in ideas_list:
        print(f'{i} - {ideas_list[i]}')


def idea_delete():
    question_delete_confirmation = input(f'Woud you like to delete existing idea enter "Y"? ')
    if question_delete_confirmation.lower() == "y":
        idea_print()
        question_delete_itemno = input(f'Eter number of idea you wish to delete > ')
        while True:
            if question_delete_itemno not in idea_list:
                print("dupa")
            else:
                with open("ideas_bank.txt", "r", encoding='utf8') as f:
                    content = f'{question_delete_itemno} |'
                with open("ideas_bank.txt", "w", encoding='utf8') as f:
                    for line in f:
                        if line.strip("\n") != content:
                            f.write(line)
    else:
        print("ok")



<<<<<<< HEAD
=======



>>>>>>> 2d003467ab73b9b6d087e0431793d5f9d3994343
def idea_start():
    """its managing function initiates the entire application"""
    print("-" * 114)
    print(geme_titele)
    user_name = input("What is your name ? ")
    if not user_name:
        print(f'\nWelcome nameless GENUISE !')
    else:
        print(f'\nWelcome {user_name.title()} !')
    print("-" * 114)
    idea_list()
    idea_print()
<<<<<<< HEAD
    # while True:
    #     idea_list()    
    #     idea_print()
    #     idea_append()
    idea_delete()

=======
    idea_append()
    idea_delete()
>>>>>>> 2d003467ab73b9b6d087e0431793d5f9d3994343
if __name__ == '__main__':
    idea_start()

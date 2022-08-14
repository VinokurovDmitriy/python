import random
from tkinter import messagebox
import tkinter as tk

global total_value, new_game_start
total_value = 2021
new_game_start = False

def player_grab_candies():
    global total_value
    candy_value = amount_candies_entry.get()
    while True:
        if candy_value == '':
            game_text['font'] = 'Calibri 10'
            game_text['text'] = 'Не стесняйся. Бери! Смотри, тут и сосательные есть...\n\n'
            return
        elif int(candy_value) > 28:
            game_text['font'] = 'Calibri 10'
            game_text['text'] = 'Не жадничай! Не больше 28, у нас уговор...\n\n'
            amount_candies_entry.delete(0, 'end')
            return
        elif int(candy_value) > total_value:
            game_text['font'] = 'Calibri 10'
            game_text['text'] = f'У меня столько нет! Остались последние {total_value}\n\n'
            amount_candies_entry.delete(0, 'end')
            return
        else:
            total_value -= int(candy_value)
            amount_candies_entry.delete(0, 'end')
            break
    if total_value < 0:
        end_game("player")
        return
    cpu_grab_candies()

def cpu_grab_candies():
    global total_value, new_game_start
    if total_value > 280:
        cpu_candies = random.randint(1,28)
    else:
        if total_value > 29:
            cpu_candies = total_value - 29
            while cpu_candies>28:
                cpu_candies %= 28
            if cpu_candies == 0: cpu_candies == 28
        elif total_value < 29:
            cpu_candies = total_value
        else: cpu_candies = total_value
    total_value -= cpu_candies
    if total_value == 0:
        end_game('cpu')
        return
    if new_game_start:
        game_text['font'] = 'Calibri 11'
        game_text['text'] = f'Тогда я возьму {cpu_candies}. Осталось всего {total_value}\nА сколько ты возьмешь?\n'
    else:
        game_text['font'] = 'Calibri 11'
        game_text['text'] = f'Оооо! Отлично! Давай я начну...\nВозьму для начала {cpu_candies}. Осталось {total_value}\n'
        new_game_start = True

def two_func_button():
    global total_value, new_game_start
    if not new_game_start:
        first_turn = random.randint(0,1)
        match first_turn:
            case 0:
                game_text['font'] = 'Calibri 14'
                game_text['text'] = 'Оооо! Отлично! Давай я начну...\n'
                player_button_grab['text'] = "ВЗЯТЬ КОНФЕТЫ"
                amount_candies_entry['state'] = tk.NORMAL
                cpu_grab_candies()
            case 1:
                game_text['font'] = 'Calibri 10'
                game_text['text'] = 'Какой хороший мальчик!\nПозволю начать тебе первым!' \
                                    '\nСколько конфет хочешь взять?\n'
                player_button_grab['text'] = "ВЗЯТЬ КОНФЕТЫ"
                amount_candies_entry['state'] = tk.NORMAL
                new_game_start = True
    else: player_grab_candies()

def new_game():
    global total_value, new_game_start
    new_game_start = False
    total_value = 2021
    cpu_player['image'] = cpu_player_photo
    game_text['font'] = 'Calibri 10'
    game_text['text'] = f"Привет, малыш! У меня есть конфетки!\nДавай сыграем в игру?\nУ меня есть {total_value} конфета, будем брать поочереди,\nно не больше 28 штук\nКто возьмет последний, тот и победил"
    amount_candies_entry['state'] = tk.DISABLED
    player_button_grab['text'] = "ДАВАЙТЕ ИГРАТЬ"
    button_restart['text'] = "УБЕЖАТЬ"
    button_restart['command'] = lambda : end_game("exit")

def end_game(winner: str):
    if winner == 'cpu':
        messagebox.showerror("Ой, конфетки кончились!", "Ты проиграл! Но не расстратвайся, пойдем ко мне домой, у меня еще много конфет! Только,тсссс...")
        cpu_player['image'] = cpu_player_end
        amount_candies_entry['state'] = tk.DISABLED
        player_button_grab['text'] = "НУ, ДАВАЙ, СУЧАРА"
        player_button_grab['command'] = new_game
        game_text['font'] = 'Calibri 11'
        game_text['text'] = "Смотрю тебе понравились сосательные конфеты\nХочешь еще разок?\n"
        button_restart['text'] = "ВЫХОД"
        button_restart['command'] = win.destroy
    if winner == 'player':
        cpu_player['image'] = player_win
        amount_candies_entry['state'] = tk.DISABLED
        player_button_grab['text'] = "ПОРОСИТЬ ЕЩЕ КОНФЕТ"
        player_button_grab['command'] = new_game
        button_restart['text'] = "ВЫХОД"
        button_restart['command'] = win.destroy
        game_text['font'] = 'Calibri 20'
        game_text['text'] = "Иди ты на хуй, мальчик!\nНи конфет, ни секса!"
    if winner == 'exit':
        cpu_player['image'] = cpu_player_exit
        amount_candies_entry['state'] = tk.DISABLED
        player_button_grab['text'] = "НАЧАТЬ ЗАНОВО"
        player_button_grab['command'] = new_game
        button_restart['text'] = "ВЫХОД"
        button_restart['command'] = win.destroy
        game_text['font'] = 'Calibri 10'
        game_text['text'] = "Спасибо, дядя! У меня диабет\nмне сладкое нельзя!\nСегодня придется руками справляться\n"

win = tk.Tk()
ico = tk.PhotoImage(file="Data/candy_ico.png")
cpu_player_photo = tk.PhotoImage(file="Data/candy_daddy.png")
cpu_player_end = tk.PhotoImage(file="Data/candy_daddy_end.png")
cpu_player_exit = tk.PhotoImage(file="Data/candy_exit.png")
player_win = tk.PhotoImage(file="Data/candy_win.png")

win.iconphoto(False, ico)
win.title("Мальчик, хочешь конфетку?")
win.geometry('420x550+900+400')
win.resizable(False,False)
win.wm_attributes("-topmost", 1)

cpu_player = tk.Label(win, image=cpu_player_photo)
game_text = tk.Label(win, text=f"Привет, малыш! У меня есть конфетки!\nДавай сыграем в игру?"
                                   f"\nУ меня есть {total_value} конфета, будем брать поочереди,"
                                   f"\nно не больше 28 штук"
                                   f"\nКто возьмет последний, тот и победил",
                         font= ('Calibri 10 bold'), background="WHITE")
amount_candies_entry = tk.Entry(win, justify='center', state=tk.DISABLED)
player_button_grab = tk.Button(win, text=f"ДАВАЙТЕ ИГРАТЬ",width=21, command=two_func_button)
button_restart = tk.Button(win, text=f"УБЕЖАТЬ",width=21, command=lambda: end_game("exit"))

cpu_player.grid(row=0)
game_text.grid(row=0, pady= 22, sticky='s')
amount_candies_entry.grid(row=5, pady=10)
player_button_grab.grid(row=7)
button_restart.grid(row=8)

win.grid_columnconfigure(0, minsize= 90)
win.mainloop()

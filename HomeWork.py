from math import pow
import curses
from curses import window
from curses.textpad import Textbox
def romanko():
    width = 100 #визначаємо ширину та символ таблиці всередині функції
    simvol = "x"
    def vvod_a(stdscr, table_x, table_y): # підфункція, в якій запитуєтья cторона
        for i in range(0,11): # цикл від 0 до 10 в якому фарбується та очищується потрібна область на екрані
            stdscr.addstr(table_y+i, table_x, " "*width) # друк width пробілів
        curses.init_pair(1,  curses.COLOR_GREEN, curses.COLOR_YELLOW) # задання колірної пари текст/фон під номером 1

        stdscr.addstr(table_y+2, table_x, "{0:{1}}".format("Сторона квадрату а = ",width)) # друк в рядку 2 від верху и table_x від лівого краю
        a = 0 # те, що ми вводимо(сторона)
        while (True): # нескінченний цикл
            try: # перевірка помилки на некоректне введення
                inputbox = curses.newwin(1,15, table_y+2, table_x+21) # область в якій пізніше буде відбуватися введення
                inputbox.bkgd(' ', curses.color_pair(1)) # встановлення в цій області колірної пари під номером 1
                box = Textbox(inputbox) # встановлення в раніше виділену область поля введення
                stdscr.refresh() # оновлення екрану для відображення змін
                box.edit() # примусове встановлення вказівника в поле введення
                a = float(box.gather()) # переведення введеного тексту в речовинне число
                if a<=0: # якщо все пройшло без помилок, це число перевіряється на менше дорівнює 0, якщо воно більше, функція завершується и повертає число S
                    stdscr.addstr(table_y+2, table_x, "{0:{1}}".format(" Число більше 0 = ",width)) # форматний рядок в який значення по черзі підставляються в фігурні дужки
                    continue
                break
            except ValueError: # якщо було введено не число видасть повідомлення, і попросить ввести знову
                stdscr.addstr(table_y+2, table_x, "{0:{1}}".format(" Введіть число = ",width))
        return a # повертає значення a

    def table(stdscr): # функція друку таблиці
        win_h, win_w = stdscr.getmaxyx() # визначення розмірів екрану
        table_x = 1 # визначення розташування на екрані таблиці у відповідності з розміром
        table_y = round(win_h/4)

        stdscr.clear() # очистка екрану
        curses.init_pair(1,  curses.COLOR_WHITE, curses.COLOR_MAGENTA) # задання кольорної пари, доступна лише всередині функції
        stdscr.attron(curses.color_pair(1)) # установка для тексту, який буде друкуватися кольорною парою

        

        a = vvod_a(stdscr, table_x, table_y) # запит сторони
        r = r = (a*pow(2, 0.5))/2 # розрахування даних за формулами
        S = ((12*r)/2)*0.5

        format = simvol + "{:^" + str(width-23-3) + "}" + simvol + "{:^23}" + simvol # задання формату виведення
        stdscr.addstr(1+table_y, table_x, simvol*width) # у відповідності з першим аргументом - номер рядка, 2 - позиція від лівого екрана, 3 - рядок, що буде виведений
        stdscr.addstr(2+table_y, table_x, format.format("Назва величини","Значення величини")) # підстановка в формат значень замість фігурних дужок
        stdscr.addstr(3+table_y, table_x, simvol*width)
        stdscr.addstr(4+table_y, table_x, format.format("Сторона квадрату","{:.2f}".format(a)))
        stdscr.addstr(5+table_y, table_x, format.format("Радіус кола r","{:.2f}".format(r)))
        stdscr.addstr(6+table_y, table_x, format.format("Площа дванадцятикутника S","{:.2f}".format(S)))
        stdscr.addstr(7+table_y, table_x, simvol*width)
        stdscr.addstr(8+table_y, table_x, format.format("Романко Максим Віталійович","БІ-244"))
        stdscr.addstr(9+table_y, table_x, simvol*width)

        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(table) # безпечний запит функції що працює з екраном


romanko() # виклик основної функції

import os
import time
import ctypes
import random
import keyboard
import pyfiglet as pf
from pyfiglet import Figlet
from termcolor import colored


# ======== CONFIG ========
Text = "Happy Birthday" # For 1000 Random Font Text Generator

os.system('color')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ======== UTILS ========
MessageBox = ctypes.windll.user32.MessageBoxW

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

# ======== ASCII ART ========
def cakefire():
    cake1 = r'''
          *                                             *
                                               *
                    *
                                  *
                                                            *
         *
                                                  *
             *
                           *             *
                                                     *
      *                                                               *
               *
    '''
    cake2 = r'''
                               (             )
                       )      (*)           (*)      (
              *       (*)      |             |      (*)
                       |      |~|           |~|      |          *
                      |~|     | |           | |     |~|
    '''
    cake3 = r'''
                      | |     | |           | |     | |
                     ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
              ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
             a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
             ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
             ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
             ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
             ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
             ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
             ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
             ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
         ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
      .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
     .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
     %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
     %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
     `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
       `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
           `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                  """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                 `%%%%%%%'
                                  `%%%%%'
                                    %%% 
                                   %%%%%
                                .,%%%%%%%,.
                           ,%%%%%%%%%%%%%%%%%%%,
    '''
    slow_print(bcolors.WARNING + cake1, 0.00010)
    slow_print(bcolors.FAIL + cake2, 0.010)
    slow_print(bcolors.OKGREEN + cake3, 0.00010)

def cake():
    cake1 = r'''
          *                                             *
                                               *
                    *
                                  *
                                                            *
         *
                                                  *
             *
                           *             *
                                                     *
      *                                                               *
               *
    '''
    cake2 = r'''
                       |      |~|           |~|      |          *
                      |~|     | |           | |     |~|
                      | |     | |           | |     | |
                     ,| |a@@@@| |@@@@@@@@@@@| |@@@@a| |.
                .,a@@@| |@@@@@| |@@@@@@@@@@@| |@@@@@| |@@@@a,.
              ,a@@@@@@| |@@@@@@@@@@@@.@@@@@@@@@@@@@@| |@@@@@@@a,
             a@@@@@@@@@@@@@@@@@@@@@' . `@@@@@@@@@@@@@@@@@@@@@@@@a
             ;`@@@@@@@@@@@@@@@@@@'   .   `@@@@@@@@@@@@@@@@@@@@@';
             ;@@@`@@@@@@@@@@@@@'     .     `@@@@@@@@@@@@@@@@'@@@;
             ;@@@;,.aaaaaaaaaa       .       aaaaa,,aaaaaaa,;@@@;
             ;;@;;;;@@@@@@@@;@      @.@      ;@@@;;;@@@@@@;;;;@@;
             ;;;;;;;@@@@;@@;;@    @@ . @@    ;;@;;;;@@;@@@;;;;;;;
             ;;;;;;;;@@;;;;;;;  @@   .   @@  ;;;;;;;;;;;@@;;;;@;;
             ;;;;;;;;;;;;;;;;;@@     .     @@;;;;;;;;;;;;;;;;@@@;
         ,%%%;;;;;;;;@;;;;;;;;       .       ;;;;;;;;;;;;;;;;@@;;%%%,
      .%%%%%%;;;;;;;@@;;;;;;;;     ,%%%,     ;;;;;;;;;;;;;;;;;;;;%%%%%%,
     .%%%%%%%;;;;;;;@@;;;;;;;;   ,%%%%%%%,   ;;;;;;;;;;;;;;;;;;;;%%%%%%%,
     %%%%%%%%`;;;;;;;;;;;;;;;;  %%%%%%%%%%%  ;;;;;;;;;;;;;;;;;;;'%%%%%%%%
     %%%%%%%%%%%%`;;;;;;;;;;;;,%%%%%%%%%%%%%,;;;;;;;;;;;;;;;'%%%%%%%%%%%%
     `%%%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%,,,,,,,%%%%%%%%%%%%%%%%%%%%'
       `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
           `%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
                  """"""""""""""`,,,,,,,,,'"""""""""""""""""
                                 `%%%%%%%'
                                  `%%%%%'
                                    %%% 
                                   %%%%%
                                .,%%%%%%%,.
                           ,%%%%%%%%%%%%%%%%%%%,
    '''
    slow_print(bcolors.WARNING + cake1, 0.000010)
    slow_print(bcolors.OKGREEN + cake2, 0.000010)

def spy():
    spy = r'''

___________________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶
___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶
________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶
_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶___¶¶¶
______¶¶¶¶__¶¶¶¶¶¶¶¶¶§§§¶______¶§¶¶¶¶¶___¶¶
_____¶_¶¶¶__¶¶¶¶¶¶¶¶§§§§§¶____¶§§¶¶¶¶¶__¶¶¶
____¶_¶¶¶___¶¶¶¶¶¶¶§§§§§77¶¶¶¶§§§¶¶¶¶¶__¶¶
_____¶¶¶____¶¶¶¶¶¶¶§§§777777§§§§¶¶¶¶¶¶_¶¶
_____¶¶______¶¶¶¶¶§777777777§§§§¶¶¶¶¶_¶¶¶
____¶¶¶_______¶¶¶¶¶77777777777§¶¶¶¶¶_¶¶¶
___¶¶¶_________¶¶¶¶¶¶§§§7777§¶¶¶¶¶¶_¶¶
__¶¶¶___________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶¶___¶¶
___________________________¶¶¶¶¶
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    '''
    slow_print(bcolors.OKGREEN + spy, 0.000010)

def hack():
    hack = r'''

     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
.... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
         
    '''
    slow_print(bcolors.FAIL + hack, 0.000010)

# ======== END OF ASCII ART ========
i1 = ''
# ======== ALL OF JOURNEY BEGIN FROM HERE ========
def scene1() :
    spy()
    i1 = input(bcolors.OKGREEN + '\nHello Good Afternoon, who are you? [Enter Your Code Name : ')
    os.system('cls')
    spy()
    i2 = input(bcolors.OKGREEN + '\nHello ' + i1 + ' Welcome to Lockanymous Agency, do you know what date is it now? ' )
    i2 = input(bcolors.OKGREEN + 'Ok ' + i1 + ' do you know what day is it?  ' )
    slow_print(bcolors.OKGREEN + 'You Wrong!!! You can Guess again!', 0.000010)
    i2 = input(bcolors.OKGREEN + '\nLets guess again what day is it?  ' )
    slow_print(bcolors.WARNING + 'ITS NOT SATURDAY!!! Guess again!', 0.000010)
    i2 = input(bcolors.OKGREEN + '  ' )
    slow_print(bcolors.FAIL + 'I ALREADY SAY ITS NOT SATURDAY!!!\nITS YOUR BIRTHDAYY SH*T!!!', 0.1)
    slow_print(bcolors.FAIL + '\nBECAUSE ITS YOUR BIRTHDAY ILL HACK YOUR COMPUTER WAHAHAHAHAHAH!!!!', 0.1)
    slow_print(bcolors.OKGREEN + '\nINJECTING VIRUS....', 0.01)
    time.sleep(3)
def scene2() :
    os.system('cls')
    hack()
    i2 = input(bcolors.OKGREEN + '\nPress ENTER button to Continue, YOU CANT ESCAPE!!!' )
    for x in range(30):
        MessageBox(None, 'HACKED!!!', 'Lockanymous', 0)
        MessageBox(None, 'YOU ARE A GENIUS HAHAHA!!!', 'Lockanymous', 0)
    for x in range(10):
        MessageBox(None, 'ARE YOU TIRED?', 'Lockanymous', 0)
        MessageBox(None, 'ARE YOU ANGRY?', 'Lockanymous', 0)
    for x in range(10):
        MessageBox(None, 'BTW HAPPY BIRTHDAY TO YOU!!!', 'Lockanymous', 0)
    i2 = input(bcolors.OKGREEN + '\nHAPPY BIRTHDAY ' + i1 + ' i wish you all the best!')
    i2 = input(bcolors.OKGREEN + '\nI hope this Surprise will be cheer up in your new age!')
    i2 = input(bcolors.OKGREEN + '\nI have Birthday Cake for you [Press Enter to Show]')
    keyboard.press('f11')
def scene3() :
    os.system('cls')
    cakefire()
    i2 = input(bcolors.OKGREEN + '\n[Press Enter to blow out the candle]')
    os.system('cls')
    cake()
    input('Press Enter to continue')
    keyboard.press('f11')
    time.sleep(3)
def scene4() :
    try:
        #==== CREDIT TO Subhankar Rakshit FROM pyseek ====
        # Enter his/her name
        Name = i1

        # Reverse your given name
        reverseText = Name[::-1]

        colorList = ['red', 'green', 'yellow', 'blue']
        timeInterval = [0.2, 0.3, 0.2, 0.4]

        # Getting all the font types from 'font.txt'
        # and storing into a list
        #==================================
        dataList = list()
        with open('fonts.txt') as f:
            for line in f:
                dataList.append(line.strip())
        #==================================

        # This part of the code prints the message
        # with different font types(fixed and randomly)
        #==================================
        for i in range(1,1000):
            if(i%10==0):
                textArt = pf.figlet_format(Text)
                print("\n", textArt)
            elif(i%9 == 0):
                textArt = pf.figlet_format(Text, font="xsbook")
                print(textArt)
            elif(i%5==0):
                F = Figlet(font=random.choice(dataList))
                textArt = colored(F.renderText(Name), random.choice(colorList))
                print("\n", textArt)
            elif(i%8==0):
                F = Figlet(font=random.choice(dataList))
                textArt = colored(F.renderText(Text), random.choice(colorList))
                print("\n", textArt)
            elif(i%7==0):
                textArt = pf.figlet_format(Text, font=random.choice(dataList))
                print("\n", textArt)
            elif(i%4==0):
                textArt = pf.figlet_format(reverseText, direction = "right-to-left")
                print("\n", textArt)
            else:
                print("")

            time.sleep(random.choice(timeInterval))
        #==================================
    except ValueError:
        print(ValueError)
        input('Press Enter to continue')
# ======== ALL OF JOURNEY END HERE ========

# ======== LETS START ALL THE SCENE ========
scene1()
scene2()
scene3()
scene4()



import pwinput
import csv
import time
import os



os.system("cls")
def clear():
    os.system('clear||cls')



    

def login():
    print('**********************************************************************************************************************************************************************')
    print('*                                      \u001b[34;1m ██╗      ██████╗  ██████╗       ██╗███╗   ██╗    ███████╗ ██████╗ ██████╗ ███╗   ███╗ \u001b[37m                                       *')
    print('*                                      \u001b[34;1m ██║     ██╔═══██╗██╔════╝       ██║████╗  ██║    ██╔════╝██╔═══██╗██╔══██╗████╗ ████║ \u001b[37m                                       *')
    print('*                                      \u001b[34;1m ██║     ██║   ██║██║  ███╗█████╗██║██╔██╗ ██║    █████╗  ██║   ██║██████╔╝██╔████╔██║ \u001b[37m                                       *')
    print('*                                      \u001b[34;1m ██║     ██║   ██║██║   ██║╚════╝██║██║╚██╗██║    ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║  \u001b[37m                                      *')
    print('*                                      \u001b[34;1m ███████╗╚██████╔╝╚██████╔╝      ██║██║ ╚████║    ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║  \u001b[37m                                      *')
    print('*                                      \u001b[34;1m ╚══════╝ ╚═════╝  ╚═════╝       ╚═╝╚═╝  ╚═══╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  \u001b[37m                                      *')
    print('**********************************************************************************************************************************************************************')
    
   
    username = input('Please Enter your Username: ')
    password = pwinput.pwinput(prompt='Please Enter your Password: ', mask='*')
    with open('database.csv') as csv_file:
        reader = csv.reader(csv_file)
        is_success = False
        for row in reader:
            if len(row) > 1:
                if row[0] == username and row[1] == password:
                    is_success = True
        
        if is_success:
            time.sleep(2.5)
            clear()
            print('\u001b[32m***********************************************************************************************************************************************************************')
            print('*                               ██╗      ██████╗  ██████╗       ██╗███╗   ██╗    ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗                            *')
            print('*                               ██║     ██╔═══██╗██╔════╝       ██║████╗  ██║    ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝                            *')
            print('*                               ██║     ██║   ██║██║  ███╗█████╗██║██╔██╗ ██║    ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗                            *')
            print('*                               ██║     ██║   ██║██║   ██║╚════╝██║██║╚██╗██║    ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║                            *')
            print('*                               ███████╗╚██████╔╝╚██████╔╝      ██║██║ ╚████║    ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║                            *')
            print('*                               ╚══════╝ ╚═════╝  ╚═════╝       ╚═╝╚═╝  ╚═══╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝                            *')
            print('*********************************************please wait a seconds...**************************************************************************************************\u001b[37m')
        
            
            
            time.sleep(3.5)

            from main2 import print_menu
            
        else:
            time.sleep(2.5)
            print('\u001b[31m**********************************************************************************************************************************************************************')
            print('*                                     ██╗      ██████╗  ██████╗       ██╗███╗   ██╗    ███████╗ █████╗ ██╗██╗     ███████╗██████╗                                    *')
            print('*                                     ██║     ██╔═══██╗██╔════╝       ██║████╗  ██║    ██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗                                   *')
            print('*                                     ██║     ██║   ██║██║  ███╗█████╗██║██╔██╗ ██║    █████╗  ███████║██║██║     █████╗  ██║  ██║                                   *')
            print('*                                     ██║     ██║   ██║██║   ██║╚════╝██║██║╚██╗██║    ██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║                                   *')
            print('*                                     ███████╗╚██████╔╝╚██████╔╝      ██║██║ ╚████║    ██║     ██║  ██║██║███████╗███████╗██████╔╝                                   *')
            print('*                                     ╚══════╝ ╚═════╝  ╚═════╝       ╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝                                    *')
            print('**********************************************************************************************************************************************************************\u001b[37m')
            time.sleep(2.5)
           
            clear()
            login()
            
             
            
        global is_exit
        global main_menu_input
        is_exit = True
        main_menu_input = ''
        time.sleep(1.5)
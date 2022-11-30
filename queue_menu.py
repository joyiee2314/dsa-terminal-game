import os
import time

def clear():
    os.system('clear||cls')
def print_menu3():
    print('**********************************************************************************************************************************************************************')
    print('*                                                                                                                                                                    *')
    print('*                                                                                                                                                                    *')
    print('*                                                       \u001b[34;1m       ██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗ \u001b[37m                                                           *')
    print('*                                                       \u001b[34;1m      ██╔═══██╗██║   ██║██╔════╝██║   ██║██╔════╝ \u001b[37m                                                           *')
    print('*                                                        \u001b[34;1m     ██║   ██║██║   ██║█████╗  ██║   ██║█████╗   \u001b[37m                                                           *')
    print('*                                                        \u001b[34;1m     ██║▄▄ ██║██║   ██║██╔══╝  ██║   ██║██╔══╝    \u001b[37m                                                          *')
    print('*                                                        \u001b[34;1m     ╚██████╔╝╚██████╔╝███████╗╚██████╔╝███████╗  \u001b[37m                                                          *')
    print('*                                                        \u001b[34;1m      ╚══▀▀═╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝  \u001b[37m                                                          *')
    print('*                                                                                                                                                                    *')
    print('*                                                              ▄█─ ─    ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                                                                     *')    
    print('*                                                              ─█─ ▄    ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                                                                     *') 
    print('*                                                              ▄█▄ █    ░█─── ░█▄▄█ ░█─░█ ──░█──                                                                     *')     
    print('*                                                                                                                                                                    *')      
    print('*                                                              █▀█ ─ 　 ░█─░█ ░█▀▀▀█ ░█──░█ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                              *') 
    print('*                                                              ─▄▀ ▄ 　 ░█▀▀█ ░█──░█ ░█░█░█ 　 ─░█── ░█──░█ 　 ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                              *') 
    print('*                                                              █▄▄ █ 　 ░█─░█ ░█▄▄▄█ ░█▄▀▄█ 　 ─░█── ░█▄▄▄█ 　 ░█─── ░█▄▄█ ░█─░█ ──░█──                              *')
    print('*                                                                                                                                                                    *')   
    print('*                                                              █▀▀█ ─   ░█▀▀█ ─█▀▀█ ░█▀▀█ ░█─▄▀                                                                      *')
    print('*                                                              ──▀▄ ▄   ░█▀▀▄ ░█▄▄█ ░█─── ░█▀▄─                                                                      *')
    print('*                                                              █▄▄█ █   ░█▄▄█ ░█─░█ ░█▄▄█ ░█─░█                                                                      *')    
    print('*                                                                                                                                                                    *')
    print('*                                                                                                                                                                    *')
    print("**********************************************************************************************************************************************************************")


    option=input("                                                                      Enter your choice:")

    if option == "1":
      print("\n")
      print('                                                                   ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                                                                      ')    
      print('                                                                   ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                                                                      ') 
      print('                                                                   ░█─── ░█▄▄█ ░█─░█ ──░█──                                                                    \n') 
  
      time.sleep(2.0)
      from wordguess import main


    elif option == "2":
      print("\n")
      print('                                                  　 ░█─░█ ░█▀▀▀█ ░█──░█ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▀█ ░█─── ─█▀▀█ ░█──░█                                                 ') 
      print('                                                  　 ░█▀▀█ ░█──░█ ░█░█░█ 　 ─░█── ░█──░█ 　 ░█▄▄█ ░█─── ░█▄▄█ ░█▄▄▄█                                                 ') 
      print('                                                  　 ░█─░█ ░█▄▄▄█ ░█▄▀▄█ 　 ─░█── ░█▄▄▄█ 　 ░█─── ░█▄▄█ ░█─░█ ──░█──                                               \n') 
      print('                                                      Wordguess is a game that can challenge the way you think                                                       ')
      print('input a letter until you finish the game and to create the given missing word, but take note that you only have 10 chances to input a wrong choice.')
      time.sleep(10)
      clear()
      print_menu3()
    elif option == "3":
     clear()
     from menu import print_menu1  
print(print_menu3())
     
import random       # I get the random module


def get_question():
    misson_names = ['SPACE TRAVEL','SOLAR PANEL ARRAY','3D PRINTING','CRATER CROSSING','EXTRACTION','SPACE STATION MODULES','SPACE WALK EMERGENCY','AEROBIC EXERCISE','STRENGTH EXERCISE','FOOD PRODUCTION','ESCAPE VELOCITY','SATELLITE ORBITS','OBSERVATORY','METEROID DEFLECTION','LANDER TOUCH-DOWN']
    while True:
        M = 'What is the Mission Name for'
        mission = random.randint(1,15)
        if mission < 10:
            print(M ,' M0' , str(mission))
            answer = input()
            if answer == misson_names[mission-1].upper(): 
                print('You got it!')
                restart = input('Do you want to try again?')
                if restart == 'NO':
                    print('Thanks for playing!')
                    break 
            else:
                print('No it was ',misson_names[mission-1],' ,do you want to try again?'.upper())
                restart = input()
                if restart == 'NO':
                   print('thanks for playing')
                   break 
        else :
            print(M , ' M' , str(mission))
            answer = input()
            if answer == misson_names[mission-1].upper() :
                print('You got it!')
                restart = input('Do you want to try again?')
                if restart == 'NO':
                    print('Thanks for playing!')
                    break 
            else:
                print('No it was ',misson_names[mission-1],', do you want to try again?'.upper())
                restart = input().upper()
                if restart == 'NO':
                   print('Thanks for playing!')
                   break 


if __name__ == "__main__":
    print('Welcome to the FLL Mission Challenge Name Game®. The objective is to remember the mission names!! You will be given the mission number and in ALL CAPS you input the mission name. Good Luck!')
    get_question()

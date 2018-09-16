import random


def get_question():
    misson_names = ['SPACE TRAVEL','SOLAR PANEL ARRAY','3D PRINTING','CRATER CROSSING','EXTRACTION','SPACE STATION MODULES','SPACE WALK EMERGENCY','AEROBIC EXERCISE','STRENGTH EXERCISE','FOOD PRODUCTION','ESCAPE VELOCITY','SATELLITE ORBITS','OBSERVITORY','METEROID DEFLECTION','LANDER TOUCH-DOWN']
    while True:
        M = 'what is the name for'
        mission = random.randint(1,15)
        if mission < 10:
            print(M ,' M0' , str(mission))
            answer = input()
            if answer == misson_names[mission - 1].upper(): 
                print('you got it!')
                restart = input('do you want to try again?')
            else:
                restart = input(' no,do you want to try again?').upper()
                if restart == 'NO' .upper():
                   print('thanks for playing')
                   break 
        else :
            print(M , ' M' , str(mission))
            answer = input()
            if answer == misson_names[mission - 1].upper() :
                print('you got it!')
                restart = input('do you want to try again?')
            else:
                restart = input('no,do you want to try again?').upper()
                if restart == 'NO' .upper():
                   print('thanks for playing')
                   break 


if __name__ == "__main__":
    get_question()

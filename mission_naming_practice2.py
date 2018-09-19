import random       # I get the random module


def get_question(): # this function will ask the question and see if it is right
    misson_names = ['SPACE TRAVEL','SOLAR PANEL ARRAY','3D PRINTING','CRATER CROSSING','EXTRACTION','SPACE STATION MODULES','SPACE WALK EMERGENCY','AEROBIC EXERCISE','STRENGTH EXERCISE','FOOD PRODUCTION','ESCAPE VELOCITY','SATELLITE ORBITS','OBSERVATORY','METEROID DEFLECTION','LANDER TOUCH-DOWN']
    while True:
        M = 'What is the Mission Name for'
        mission = random.randint(1,15)
        if mission < 10:
            order1 = random.randint(1,3)
            order2 = random.randint(1,3)
            order3 = random.randint(1,3)
            if order1 == order2:
                order1 = random.randint(1,3)
            elif order2 == order3:
                order2 = random.randint(1,3)
            elif order3 == order1:
                order3 = random.randint(1,3)
            choices1 = random.randint(1,15)
            choices2 = random.randint(1,15)
            if choices1 == mission:
                choices1 = random.randint(1,15)
            elif choices1 == choices2:
                choices2 = random.randint(1,15)
            elif choices2 == mission:
                mission = random.randint(1,15)
            print(M ,' M0' , str(mission))
            if order1 == 1 and order2 == 2 and order3 == 3:
                print('\t1.',misson_names[mission - 1],'\n\t2.',misson_names[choices1 - 1],'\n\t3.',misson_names[choices2 - 1])
                answer = input()
            elif order1 == 2 and order2 == 3 and order3 == 1:
                print('\t1.',misson_names[choices1-1],'\n\t2.',misson_names[choices2-1],'\n\t3.',misson_names[mission-1])
                answer = input()
            else:
                print('\t1.',misson_names[choices2-1],'\n\t2.',misson_names[mission-1],'\n\t3.',misson_names[choices1-1])
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
            order1 = random.randint(1,3)
            order2 = random.randint(1,3)
            order3 = random.randint(1,3)
            if order1 == order2:
                order1 = random.randint(1,3)
            elif order2 == order3:
                order2 = random.randint(1,3)
            elif order3 == order1:
                order3 = random.randint(1,3)
            choices1 = random.randint(1,15)
            choices2 = random.randint(1,15)
            if choices1 == mission:
                choices1 = random.randint(1,15)
            elif choices1 == choices2:
                choices2 = random.randint(1,15)
            elif choices2 == mission:
                mission = random.randint(1,15)
            print(M ,' M' , str(mission))
            if order1 == 1 and order2 == 2 and order3 == 3:
                print('\t1.',misson_names[mission - 1],'\n\t2.',misson_names[choices1 - 1],'\n\t3.',misson_names[choices2 - 1])
                answer = input()
            elif order1 == 2 and order2 == 3 and order3 == 1:
                print('\t1.',misson_names[choices1-1],'\n\t2.',misson_names[choices2-1],'\n\t3.',misson_names[mission-1])
                answer = input()
            else:
                print('\t1.',misson_names[choices2-1],'\n\t2.',misson_names[mission-1],'\n\t3.',misson_names[choices1-1])
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

if __name__ == "__main__":
    print('Welcome to the FLL Mission Challenge Name Game®. The objective is to remember the mission names!! You will be given the mission number and choises and in ALL CAPS you input the mission name. Good Luck!')
    get_question()

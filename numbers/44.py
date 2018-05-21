import time
#TODO: fix bug

def ask(question,variable,string):
    print(question)
    if string == 'no':
        variable = int(input())
    # else:
    #     variable = input()

def main():
    ask('what is the year you want?','year','no')
    # ask('what is the month you want?','month','yes')
    # ask('what is the day of month you want?','day_of_month','no')
    # ask('what is the hour you want?','hour','no')
    # ask('what is the minute you want?','minute','no')
    # ask('what is the second you want?','second','no')
    # t=('year','month','day_of_month','hour','minute','second',0,0,0)
    # print(time.asctime(t))

if __name__ == '__main__':
    main()



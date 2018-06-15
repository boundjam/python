import time as ti
#TODO: fix bug

def ask(question,string):
    print(question,end=' ')
    if string == 'no':
        variable = int(input())
    else:
        variable = input()
        return variable

def main():
    year=ask('what is the year you want? : ','no')
    month=ask('what is the month you want? :','yes')
    day_of_month=ask('what is the day of month you want? :','no')
    hour=ask('what is the hour you want? :','no')
    minute=ask('what is the minute you want? :','no')
    second=ask('what is the second you want? : ','no')
    t = (year, month, day_of_month, hour, minute, second, 0, 0, 0)
    print(ti.asctime(t))

if __name__ == '__main__':
    main()



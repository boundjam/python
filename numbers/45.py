import time
print(time.time())
def lots_of_numbers(max):
    starting=time.time()
    for x in range(0,max):
        print(x)
    ending=time.time()
    number= ending - starting
    print(f'it took {number} seconds')
lots_of_numbers(10)

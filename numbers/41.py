ingredients = ['snails','leeches','gorrila belly-button lint','caterpillars','centipede toes']
i=len(ingredients)
num=0
for x in range(0,i):
    if num >= i:
        break
    m=ingredients[num]
    print(num, m)
    num=num+1

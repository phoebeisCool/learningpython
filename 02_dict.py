money_spent = {'Grocery':150,'Lipstic':50,'Software':1150}
money_spent['Mood'] = 30

for key,value in money_spent.items():
    if value > 100:
        print(key)
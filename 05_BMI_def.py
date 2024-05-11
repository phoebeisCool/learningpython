def BMI_calcultor(weight,height):
    bmi = weight / height**2
    if bmi <= 18:
        category = "偏瘦"
    elif bmi <25 :
        category = '正常'
    elif bmi <30:
        category = '偏胖'
    else:
        category = '肥胖'
    print(f'你的体型：{category}')
    return round(bmi,1)

BMI_calcultor(60,1.6)


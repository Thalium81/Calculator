def calc(text):
    #создание словаря чисел
    num = {
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
        "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
        "десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13,
        "четырнадцать": 14, "пятнадцать": 15, "шестнадцать": 16,
        "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
        "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
        "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
        "сто": 100, "двести": 200, "триста": 300, "четыреста": 400, "пятьсот": 500,
        "шестьсот": 600, "семьсот": 700, "восемьсот": 800, "девятьсот": 900,
        "одна тысяча":1000,"две тысячи":2000, "три тысячи":3000,"четыре тысячи":4000,
        "пять тысяч":5000, "шесть тысяч":6000, "семь тысяч":7000,"восемь тысяч":8000,
        "девять тысяч":9000
    }
    #изменение знаков
    text = text.replace("минус","-").replace("плюс","+").replace("умножить на","*")
    text = text.split()
    text.append("#")
    #изменение чисел
    flag = False
    text2 = []
    num_proc = 0

    for element in text:
        if element in "-+*":
            
            text2.append(num_proc)
            num_proc = 0
            text2.append(element)
            
        elif element == "#":
            text2.append(num_proc)
            num_proc = 0
            
        else:
            num_proc += num[element]
            
    #умножение
    
    while "*" in text2:
        text3 = text2[:text2.index("*")-1]
        text3.append(int(text2[text2.index("*")-1])*int(text2[text2.index("*")+1]))
        text3 += text2[text2.index("*")+2:]
        text2 = text3
        
    #сложение и вычитание
            
    text3 = []
    for index in range(len(text2)):
        if text2[index] == "-":
            text2[index] = 0
            text2[index+1] = 0 - text2[index+1]
        if text2[index] == "+":
            text2[index] = 0
    
    ans = sum(text2)
    
    #обратный словарь чисел
    num_rev = dict(zip(num.values(), num.keys()))
    #ответ в  текст
    ans_text = []
    if len(str(ans)) == 4:
        ans_text.append(str(ans)[-4]+"000")
    if len(str(ans)) >= 3 and str(ans)[-3] != "0":
        ans_text.append(str(ans)[-3]+"00")
    if len(str(ans)) >= 2 and str(ans)[-2] != "0":
        if str(ans)[-2] == "1":
            ans_text.append(str(ans)[-2] + str(ans)[-1])
        else:
            ans_text.append(str(ans)[-2] + "0")
        if str(ans)[-2] != "1" and str(ans)[-1] != "0":
            ans_text.append(str(ans)[-1])
    if len(str(ans)) == 1 or str(ans)[-2] == "0":
        if str(ans)[-1] == "0" and len(str(ans)) == 1:
            ans_text.append(str(ans)[-1])
        elif str(ans)[-1] != "0":
            ans_text.append(str(ans)[-1])
        
    
    output=""
    for numb in ans_text:
        output+=num_rev[int(numb)]+" "
    return output
    
while True:
    print(calc(input("Введите выражение: ").lower()))

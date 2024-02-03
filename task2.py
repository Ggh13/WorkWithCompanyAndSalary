import csv
def qSort(m, re=0): # Функция быстрой сортировка
    if(re >= 100): # Берем предел рекурсий
        return m
    if(len(m) <= 1): ## Если массив длина 1
        return m
    k = m[len(m) // 2] # Берем элемент для сравнения
    l = []
    r = []
    mid = []
    for i in m:
        if(i > k):
            r.append(i) # если элемент больше опроного добавляем в один массив или в другой
        elif i == k:
            mid.append(k)
        else:
            l.append(i) # или меньше
    #print(l, r)
    #input()
    re += 1
    return qSort(l, re) + mid + qSort(r, re) # повторяем пока не отсортируем



#print(f.readline())
d = {}
m = []
s = {}
f = open("vacancy.csv", encoding="utf-8") # открываем файл
for v in f.readlines(): 
    i = v.strip().split(";")
    if i[-1] in d:   # считаем кол во рабочих в компании
        d[i[-1]] += 1
    else:
        d[i[-1]] = 1
    if "классный руководитель" == i[3]: # компании в которых есть класс рук
        s[i[-1]] = i[0]
        m.append(i[-1]) # запоминаем эти компании
sp = []
for i in m:
    sp.append(d[i]) # массив кол во людей в компании в которых есть класс рук
#print(len(sp))
nsp = qSort(sp) # сортируем
#print(nsp)
for i in m:
    if(d[i] == nsp[0]): # если в этой компании минимальное кол во людей выводим
        print("В компании " +  i + " есть заданная профессия: " + "классный руководитель" + ", з/п в такой компании составит: " + s[i] )
    
input()

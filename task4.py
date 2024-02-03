import csv
def indToProc(f1):
    f = open(f1, encoding="utf-8") 
    f.readline()
    data = []
    d = {}
    dc = {}
    for v in f.readlines(): 
        i = v.strip().split(";")            
        data.append([i[0], i[1], i[2], i[3]])
        if i[1] in d:   
            d[i[1]] += int(i[0])# Смотрим сколько всего денег получает конкретный тип
            dc[i[1]] += 1
        else:
            d[i[1]] = int(i[0])
            dc[i[1]] = 1
    sd = {}
    pcd = {}
    for i in d:
        sd[i] = d[i] / dc[i] # Высчитываем ср арефм


    d = open("vacancy_procent.csv", 'w', newline='') # Создаем новый файл
    w = csv.writer(d)

    f = open(f1, encoding="utf-8") 
    f.readline()
    ds = 0
    for v in f.readlines():
        i = v.strip().split(";")
        pcd[i[1]] = int(i[0]) / sd[i[1]] * 100 # считаем в процентах сколько составляет
        data[ds] = data[ds] + [int(pcd[i[1]])] 
        w.writerow(data[ds]) # Записыаем в новый файл значения
        ds += 1
    d.close()
fileName = "vacancy.csv"
indToProc(fileName)

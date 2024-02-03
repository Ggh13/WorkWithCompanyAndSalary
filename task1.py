import csv
f = open("vacancy.csv", encoding="utf-8")
f.readline()
d = {}
for v in f.readlines():
    i = v.strip().split(";")
    if i[-1] in d: 
        if(d[i[-1]][0] < int(i[0])): # ищем максимальную ЗП
            d[i[-1]] = [int(i[0]), i[3]]
    else:
       
        d[i[-1]] = [int(i[0]), i[3]] 
m = []
for i in d:
    m.append([i.strip(), d[i][1], d[i][0]]) 
m.sort(key=lambda x: -x[2]) # сортируем по ЗП
for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        m[i][j] = str(m[i][j])
print(" - ".join(m[0])) # Выводим тройку лидеров
print(" - ".join(m[1]))
print(" - ".join(m[2]))
with open("vacancy_new.csv",'w', encoding="utf-8", newline='') as d:
    w = csv.writer(d) # Записываем в новый файл 
    for i in m:
        w.writerow(i)
    

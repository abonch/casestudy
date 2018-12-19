## В этом файле мы читаем названия файлов из директории, выводим из на экран, выводим количество файлов, выводим количество символов
## в каждом файле. Для того, чтобы сравнить количество символов, мы заводим словарь, где ключ - название файла, а значений кол-во символов в файле
## мы сортируем словарь в обратном порядке и выводим результат на экран.


import os
filelist = os.listdir("../../TEI/fiction_and_essays")
path = "../../TEI/fiction_and_essays/"
d = {} #это мы создали словарь, чтобы туда записывать значения разных элементов, а потом их сравнить и т.д.
for filename in filelist:
    openfile = open(path+filename)
    content = openfile.read()
    openfile.close()
    print(filename)
    print(len(content))
    d[filename] = len(content)
print(len(filelist))
for filename in sorted(d, key=d.get, reverse=True): #filename мне больше не нужна, но я ее беру, потому что по смыслу это она.
    #мы достаем значения из словаря с помощью функции d.get, это и есть key - то, по чему сортируем, сортировка должна быть в обратном порядке (reverse=True)
    print(filename, d[filename])
#print(filelist)
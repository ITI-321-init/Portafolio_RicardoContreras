"""================================================================================================
University...: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de la Información
Course.......: ITI-321 - Programación II
Period.......: 3-2024
Document.....: Read-Write/main.py
Goals........: read & write process
Professor....: Jorge Ruiz (york)
Student......: Ricardo Contreras
================================================================================================"""




#File Objects

#Method 1: contex manager: its cosed the file pn its own
print('--------------(Reading)--------------')



with open('test-1.txt', 'r') as f:
    print('=======================================')
    print('for start')
    for line in f:
        print(line, end='')
    print('for end')

    print('=======================================')
    f_contents = f.read()
    print(f_contents)
    print('=======================================')

#Method 2: traditional way : does not close the file, user need to
#f = open('test-1.txt', 'r')

print(f.name)
print(f.mode)
print(f.closed)

#file need to be closed every time, if no, its can course leaks and errors.
#use a contex manager instead
#f.close()


print('--------------(Writing)--------------')

#while using the write expression, if file doesn't exist, its will be created its own
#if file exist, its will be overwritten, in that case use 'wa' instead of 'w'
with open('test-2.txt', 'r+') as j:
    print('--------------(Writing)--------------')
    print('On code')
    j.write('Test')
    j.write('Again')
    print('--------------(Writing)--------------')


# Using Write and Read on test-1

#copy a TEXT document
with open('test-1.txt', 'r') as rf:
    with open('test-1_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

#copy a IMAGE document
with open('Asahi.jpg', 'rb') as rf:
    with open('Asahi-copy.jpg', 'wb') as wf:
        for line in rf:
            wf.write(line)









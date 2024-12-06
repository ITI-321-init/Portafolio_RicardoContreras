"""================================================================================================
University...: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de la Información
Course.......: ITI-321 - Programación II
Period.......: 3-2024
Document.....: Exception-Handling/EH_Main.py
Goals........: Error Handling
Professor....: Jorge Ruiz (york)
Student......: Ricardo Contreras
================================================================================================"""

#---------------------------------(Basic Error Handling)---------------------------------
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int (input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero")
except ValueError as e:
    print(e)
    print('Only enter numbers')
except Exception as e:
    print(e)
    print("Something went wrong ")
else:
    print(result)
finally:
    print('This block will always execute')


#You can use this code to help with file manipulation, there's a 'Finally' module that will always execute, 'finally' module que be used to get back to rook directory instead to do it manually
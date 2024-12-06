#   Functions and classes can be imported and reused without the main block
#   of code executing improving modularity, readability and leaves no global variables and
#   avoid unintended execution

def favorite_food(food):
    print(f'My favorite food is {food}')


def main():
    print('This is script1')
    favorite_food('Pizza')
    print('Good Buy')

if __name__ == '__main__':
    main()
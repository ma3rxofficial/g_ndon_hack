import config

def menu():
    print(config.logo + '\n')
    print(config.funcs_menu + '\n')

    choosed_func = str(input('Input function: '))


    config.func_parse(choosed_func)

if __name__ == '__main__':
    menu()
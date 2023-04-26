'''
(За основу можна використати заняття №3) Створити клас, який за замовчуванням міститиме
атрибутами- словник та кортеж.

Далі створити методи, за допомогою яких доступні всі взаємодії (тобто всі методи) доступні
для цих типів даних. Також передбачено два рівні доступу- юзер / адмін. Юзеру доступні
тільки самі атрибути, адміну (при введенні логін + пароль) доступні всі методи для використання.

Кожен крок знаходиться в окремому методі та відповідно викликається за необхідності.
Кожен метод передбачає наявність можливості- перейти в інший метод
(для цього можна використати додаткове меню).

Якщо для взаємодії необхідна інша послідовність (список, кортеж, словник, сет)- значить
ми маємо можливість передати таку послідовність.

Також адмін може додати нові елементи до наявного кортежу. Не забуваємо, що словник
не може містити двох однакових ключів, відповідно при спробі додати наявний ключ- виводимо
питання- чи бажаємо ми змінити значення наявного ключа?
'''

class Main:
    def __init__(self):
        self.dct = {'key1': 'value1',
                    'key2': 'value2',
                    'key3': 'value3'}
        self.t = (1, 2, 3, 'a', 'b', 'c')

    def menu(self):
        print('1. user')
        print('2. admin')
        self.a = int(input('enter a number: '))
        if self.a == 1:
            print(self.dct)
            print(self.t)
        elif self.a == 2:
            self.admin_func()

    def admin_func(self):
        self.login, self.password = input('Enter your login and password: ').split()
        if self.login == 'python' and self.password == 'developer':
            print('Login was successful ')
            self.type_func()
        else:
            print('Invalid login or password')

    def type_func(self):
        print('1. dict')
        print('2. tuple')
        self.type = int(input('enter number: '))
        if self.type == 1:
            self.admin_dict_func()
        elif self.type == 2:
            self.tuple_func()

    def admin_dict_func(self):
        print(self.dct)
        self.option = input('Choose an interaction option (get, pop, copy, clear, items, keys, values, setdefault, update): ')
        if self.option == 'get':
            get_option = input('enter the key: ')
            print(self.dct.get(get_option))
        elif self.option == 'pop':
            pop_option = input('enter the key: ')
            print(self.dct.pop(pop_option))
        elif self.option == 'copy':
            print(self.dct.copy())
        elif self.option == 'clear':
            print(self.dct.clear())
        elif self.option == 'items':
            print(self.dct.items())
        elif self.option == 'keys':
            print(self.dct.keys())
        elif self.option == 'values':
            print(self.dct.values())
        elif self.option == 'setdefault':
            self.key, self.value = input('enter the key and value: ').split()
            print(self.dct.setdefault(self.key, self.value))
        elif self.option == 'update':
            self.key, self.value = input('enter the key and value: ').split()
            print(self.dct.update({self.key: self.value}))

    def tuple_func(self):
        print(self.t)
        self.option = input('Choose an interaction option (index, count): ')
        if self.option == 'index':
            self.index_type = input('what type do you want to output? (int, str): ')
            if self.index_type == 'int':
                self.index_option = int(input('enter the value: '))
                print(self.t.index(self.index_option))
            elif self.index_type == 'str':
                index_option = input('enter the value: ')
                print(self.t.index(index_option))
        elif self.option == 'count':
            self.count_type = input('what type do you want to output? (int, str): ')
            if self.count_type == 'int':
                count_option = int(input('enter the value: '))
                print(self.t.count(count_option))
            elif self.count_type == 'str':
                count_option = input('enter the value: ')
                print(self.t.count(count_option))

n = Main()
n.menu()




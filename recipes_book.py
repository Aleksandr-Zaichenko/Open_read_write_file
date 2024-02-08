# Функция к Задаче №1, чтение рецептов из файла и получение словаря

def cook_book_read(book_src):
    with open(book_src) as recipes:
        recipes_dict = {}
        for line in recipes.read().split('\n\n'):
            dish, q_portion, *ingredients = line.split('\n')
            ing_list = []
            for ing in ingredients:
                ingredient_name, quantity, measure = ing.split('|')
                ing_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            recipes_dict[dish] = ing_list
    return recipes_dict

cook_book = cook_book_read('recipes.txt')

print(cook_book)

# Функция к Задаче №2, принимает список блюд и количество персон

def get_shop_list_by_dishes(dishes, person_count):
    cooked_dish = {}
    for name in cook_book:
        for dish in dishes:
            if name == dish:
                for item in cook_book[name]:
                    ing, me, qu = item['ingredient_name'], item['measure'], int(item['quantity'])
                    cooked_dish.setdefault(ing,{'measure':me, 'quantity':qu*person_count})
    return cooked_dish

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задача №3, создаём список файлов для объединения, и целевой файл для записи результата

files_list = ['1.txt', '2.txt', '3.txt']
target_file = 'merging_files.txt'

# Функция для подсчёта количества строк в файле

def count_lines(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

# Функция слияния файлов, принимает список файлов для объединения и целевой файл

def merging_files(files_list, target_file):
    files_dict = {}
    for item_fl in files_list:
        with open(item_fl) as txt_file:
            files_dict.setdefault(count_lines(item_fl), [item_fl, txt_file.read()])
    f_dict_sorted = dict(sorted(files_dict.items()))
    for c_lin, list_fl in f_dict_sorted.items():
        with open(target_file, 'a') as sorted_file:
            sorted_file.write(f"{list_fl[0]}\n{c_lin}\n{list_fl[1]}\n")

merging_files(files_list, target_file)

# Проверяем результат работы функции merging_files

with open (target_file) as result_fl:
    for line in result_fl:
        print(line.strip())
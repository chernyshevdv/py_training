# Некоторые ключевые takeaways

* modify_list.py
  * `lst[:] = [1,2,3]` заменяет комоненты lst
  * `[x for x in lst if x != 0]` фильтрует что брать
* lcd.py
  * `print("smth", end='')` убирает `\n` из вывода
  * `print(*[1,2,3], sep=' ')` раскрывает список, разделяя его значения пробелами. Эта конструкция выдаст такой результат: `1 2 3`
* length_stats.py:
  * парсим ввод: `input().strip().lower().split(' ')`.
  При вводе `"Ab cD EF"`, получим список: `['ab', 'cd', 'ef']`
  * `sorted(lst)` сортирует список (да и set тоже)
  * `collections.Counter(lst)` считает частоту элементов и выдаёт в виде кортежей `(val, freq)`
* rle.py
  * полезные RegExp:
    * `\d`: цифры
    * `\D`: не цифры
  * `re.findall(pattern, source)` выдает список кортежей групп. 
  Пример: `re.findall(r"(\d*)(\D)", "a2b14cg")` выдаст вот такой список:
  `[('', 'a'), ('2', 'b'), ('14', 'c'), ('', 'g')]`
  * `'c' * 4` даст строку `"cccc"`
* duplicates.py
  * получить числа из stdin: `args = [int(x) for x in input().split()`
* analyze_crimes.py
  * `csv.DictReader` позволяет читать из csv dict с заголовками из первой строки
* artsy.py
  * `for line in sys.stdin:` читает stdin построчно
  * Если `data` - dict, то `data.items()` выдаст список кортежей `(key, value)`
  * Хитрая сортировка списка: `sorted(data.items(), key=lambda kv: kv[0]+kv[1])`.
  Отсортирует словарь по "склейке" ключа и значения.
  Можно задать какую угодно лямбду.
  * Вообще, тут хорошо взять пример работы с JSON
* cards.py - пример реализации класса с переопределением операторов.
* class_parents.py
  * рекурсия с инициализацией стека `visited` внутри функции
* count_words.py - простейший пример `collections.Counter`
* cubes.py - простейший примеры работы с XML
* jolly.py
  * Пример нахождения разницы множеств `set.symmetric_difference(other)`
* marks.py
  * Форматирование дробных чисел: `"{:.2f}".format(2.2335)` даст 2.23
* math_op.py - реализация анализатора командной строки через словарь токенов и функций
* underscore_to_camelcase.py
  * Капитализация `str.title()` слов в строке: "one two three" -> "One Two Three"
* mul_list_index_search.py:
  * `print(*sublist or ['None'])` печатает содержимое списка sublist через пробел. Если список пустой - выводит 'None'. 
  Фишка - в operator precedence: приоритет `or` выше, чем `*`, 
  получается вот такая расстановка скобок: `print(*(sublist or ['None']))`
* RLE_encode.py
  * Поиск повторяющихся символов RegExp'ом: `r"((\w)\2*)"`. 
  `re.findall()` даст группы вида `[('aaa', 'a'), ('b', 'b')]`
* collatz.py
  * _generators_!
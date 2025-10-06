# Ввід кількості елементів
n = int(input("Введіть кількість чисел (від 7 до 20): "))
while n < 7 or n > 20:
    print("Помилка! Кількість повинна бути від 7 до 20.")
    n = int(input("Введіть кількість чисел (від 7 до 20): "))

# Ввід чисел
print(f"Введіть {n} цілих чисел від 0 до 100 через пробіл:")
A_input = list(map(int, input().split()))

# Перевірка
while len(A_input) != n or any(x < 0 or x > 100 for x in A_input):
    print(f"Помилка! Потрібно ввести рівно {n} чисел у діапазоні 0–100.")
    A_input = list(map(int, input().split()))

A1 = A_input.copy()   # для Лістинг 1.3
arr = A_input.copy()  # для Лістинг 1.4

# ============================
# Лістинг 1.3 — Чисельне моделювання псевдокоду
# ============================
print("\n\n=== Лістинг 1.3 — Чисельне моделювання псевдокоду ===")
print(f"Вихідні дані A={A1} n={n}")
print(f"A.length={len(A1)} (for j)")

comparisons = 0
assignments = 0

for j in range(1, n):
    key = A1[j]
    assignments += 1  # присвоєння key
    i = j - 1
    print(f"{j}. j = {j}; key = A[{j}] = {key}; i = {j} – 1 = {i};")

    while i >= 0 and A1[i] > key:
        comparisons += 1
        print(f"i>0 (True) A[{i}] > key ({A1[i]} > {key} – True) → A[{i+1}] = A[{i}] = {A1[i]};")
        A1[i+1] = A1[i]
        assignments += 1
        print(f"A={A1}")
        i -= 1
        if i >= 0:
            print(f"i = {i+1} – 1 = {i};")

    if i >= 0:
        comparisons += 1
        print(f"i>0 (True) A[{i}] > key ({A1[i]} > {key} – False);")
    else:
        print(f"i>0 (False)")

    A1[i+1] = key
    assignments += 1
    print(f"A[{i+1}] = key = {key}")
    print(f"A={A1}")

print("(End for j)")

print("\nСтатистика (Лістинг 1.3):")
print(f"Загальна кількість порівнянь: {comparisons}")
print(f"Загальна кількість присвоєнь: {assignments}")

# ============================
# Лістинг 1.4 — Трасування Python-коду
# ============================
print("\n\n=== Лістинг 1.4 — Трасування Python-коду ===")
print(f"Початковий масив: {arr}")
print("-" * 30)

comparisons2 = 0
assignments2 = 0

for j in range(1, len(arr)):
    key = arr[j]
    assignments2 += 1
    i = j - 1
    print(f"Ітерація {j}:")
    print(f" Елемент для вставки (key): {key}")
    print(f" Відсортована частина: {arr[:j]}")

    while i >= 0:
        comparisons2 += 1
        if arr[i] > key:
            print(f" Порівняння: {arr[i]} > {key}. True. Зсуваємо {arr[i]} вправо.")
            arr[i+1] = arr[i]
            assignments2 += 1
            i -= 1
        else:
            print(f" Порівняння: {arr[i]} > {key}. False. Цикл завершено.")
            break
    if i < 0:
        print(f" Досягнуто початку масиву. Цикл завершено.")

    arr[i+1] = key
    assignments2 += 1
    print(f" Вставка {key} на позицію {i+1}.")
    print(f" Масив після ітерації {j}: {arr}")
    print("-" * 30)

print("Сортування завершено.")
print(f"Фінальний відсортований масив: {arr}")

print("\nСтатистика (Лістинг 1.4):")
print(f"Загальна кількість порівнянь: {comparisons2}")
print(f"Загальна кількість присвоєнь: {assignments2}")

print("\nПеревірка узгодженості підрахунків:")
print(f"Порівняння: Лістинг1.3={comparisons}  Лістинг1.4={comparisons2}")
print(f"Присвоєння: Лістинг1.3={assignments}  Лістинг1.4={assignments2}")

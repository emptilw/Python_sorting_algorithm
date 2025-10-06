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

# Робочі копії для обох лістингів
A1 = A_input.copy()   # для Лістинг 1 (чисельне моделювання псевдокоду)
arr = A_input.copy()  # для Лістинг 2 (трасування Python-коду)


# --------------------------
# Лістинг 1 – Чисельне моделювання псевдокоду
# --------------------------
print("\n\n=== Лістинг 1 — Чисельне моделювання псевдокоду ===")
print(f"Вхідні дані A={A1} n={n}")
print("(for i)")

comparisons = 0
assignments = 0

# Selection Sort з детальним виводом (згідно з псевдокодом)
for i in range(n - 1):
    min_index = i
    # початкова перевірка j = i+1
    print(f"{i+1}. i={i}; min={min_index}; j={i}+1={i+1}; ", end="")
    comparisons += 1
    if A1[i+1] < A1[min_index]:
        print(f"A[{i+1}]<A[{i}] ({A1[i+1]}<{A1[min_index]}) min={i+1}")
        min_index = i+1
        assignments += 1     # рахувати оновлення min_index
    else:
        print(f"A[{i+1}]<A[{i}] ({A1[i+1]}<{A1[min_index]}) min={min_index}")

    # цикл по j починаючи з i+2
    for j in range(i+2, n):
        letter = chr(95 + (j - i))  # a, b, c...
        print(f"{letter}) j={j} A[{j}]<A[{min_index}] ({A1[j]}<{A1[min_index]})", end=" ")
        comparisons += 1
        if A1[j] < A1[min_index]:
            min_index = j
            assignments += 1    # рахувати оновлення min_index
            print(f"min={min_index}")
        else:
            print(f"min={min_index}")

    print("(end for j)")

    # обмін
    if min_index != i:
        b = A1[i]
        assignments += 1
        print(f"b=A[{i}]")
        A1[i] = A1[min_index]
        assignments += 1
        print(f"A[{i}]=A[{min_index}]")
        A1[min_index] = b
        assignments += 1
        print(f"A[{min_index}]=b A[{i}]={A1[i]} A[{min_index}]={A1[min_index]}")
    print(f"A={A1}")

print("(end for i)")

# Вивід статистики Лістинг 1
print("\nСтатистика (Лістинг 1):")
print(f"Кількість операцій порівняння: {comparisons}")
print(f"Кількість операцій присвоювання: {assignments}")

# --------------------------
# Лістинг 2 – Трасування Python-коду (людяний опис)
# --------------------------
print("\n\n=== Лістинг 2 — Трасування Python-коду ===")

# Лічильники для Лістинг 2
comparisons2 = 0
assignments2 = 0

print(f"Початковий масив: {arr}")
print("-" * 30)

# Selection Sort з пояснювальним виводом,
# але з тим же способом підрахунку операцій:
for i in range(len(arr) - 1):
    min_idx = i
    print(f"Ітерація {i}:")
    print(f" Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
    print(f" Шукаємо мінімальний елемент у частині: {arr[i:]}")

    # Пошук мінімального елемента — рахунок порівнянь і присвоєнь при оновленні мінімуму
    # (цей цикл дає ті самі перевірки, що й у Лістинг 1)
    for j in range(i + 1, len(arr)):
        comparisons2 += 1
        if arr[j] < arr[min_idx]:
            min_idx = j
            assignments2 += 1   # рахувати оновлення min_idx

    print(f" Знайдено мінімальний елемент: arr[{min_idx}] = {arr[min_idx]}")

    # Обмін (якщо потрібно) — показуємо детально, як у прикладі
    if min_idx != i:
        print(f" Обмін arr[{i}] ({arr[i]}) і arr[{min_idx}] ({arr[min_idx]})")
        b = arr[i]            # присвоєння 1
        assignments2 += 1
        arr[i] = arr[min_idx] # присвоєння 2
        assignments2 += 1
        arr[min_idx] = b      # присвоєння 3
        assignments2 += 1

    print(f" Масив після ітерації {i}: {arr}")
    print("-" * 30)

print("Сортування завершено.")
print(f"Фінальний відсортований масив: {arr}")

# Вивід статистики Лістинг 2
print("\nСтатистика (Лістинг 2):")
print(f"Кількість операцій порівняння: {comparisons2}")
print(f"Кількість операцій присвоювання: {assignments2}")

# Додатковий контроль: показати чи збігаються підрахунки між лістингами
print("\nПеревірка узгодженості підрахунків:")
print(f"Порівняння: Лістинг1={comparisons}  Лістинг2={comparisons2}")
print(f"Присвоєння: Лістинг1={assignments}  Лістинг2={assignments2}")
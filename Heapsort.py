# --- Глобальні лічильники для моделювання ---
import matplotlib.pyplot as plt
import networkx as nx

comparisons = 0
assignments = 0
step = 1

# --- ВІЗУАЛІЗАЦІЯ КУПИ ---
def draw_heap(A, highlight=None, sorted_part=None):
    global step
    n = len(A)
    G = nx.Graph()
    labels = {}

    for i in range(n):
        G.add_node(i)
        labels[i] = A[i]

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            G.add_edge(i, left)
        if right < n:
            G.add_edge(i, right)

    pos = {}
    level = 0
    i = 0
    while i < n:
        nodes_on_level = 2 ** level
        for j in range(nodes_on_level):
            if i >= n:
                break
            pos[i] = (j, -level)
            i += 1
        level += 1

    plt.figure(figsize=(9, 6))
    colors = []
    for i in range(n):
        if highlight and i in highlight:
            colors.append("orange")
        elif sorted_part and i >= sorted_part:
            colors.append("lightgray")
        else:
            colors.append("skyblue")

    nx.draw(G, pos, labels=labels, node_color=colors, node_size=1000, with_labels=True)

    array_colors = []
    for i in range(n):
        if highlight and i in highlight:
            array_colors.append("orange")
        elif sorted_part and i >= sorted_part:
            array_colors.append("lightgray")
        else:
            array_colors.append("skyblue")

    for i, val in enumerate(A):
        plt.text(i * 0.6, -level - 0.7, str(val), ha="center",
                 va="center", fontsize=13,
                 bbox=dict(facecolor=array_colors[i], boxstyle="round,pad=0.3"))

    plt.title(f"Крок {step}")
    step += 1
    plt.axis("off")
    plt.show()


# --- ТРАСУВАННЯ + МОДЕЛЮВАННЯ САМЕ В sink() ---
def sink(A, i, n, trace_logs, phase):
    global comparisons, assignments

    k = i
    j = 2 * k + 1

    if j < n:
        trace_logs.append(f"Починаємо 'занурювати' елемент: {A[i]} з індексу {i}")

    while j < n:
        if j < n - 1:
            comparisons += 1
            trace_logs.append(f"Порівнюємо {A[j]} (лівий) та {A[j+1]} (правий).")
            if A[j] < A[j + 1]:
                j = j + 1

        comparisons += 1
        trace_logs.append(f"Порівнюємо батька {A[k]} та найбільшого дочірнього {A[j]}.")

        if A[k] >= A[j]:
            trace_logs.append(f"{A[k]} (батько) >= {A[j]} (дочірній). Елемент на місці.")
            break
        else:
            trace_logs.append(f"Міняємо місцями {A[k]} (батько) та {A[j]} (дочірній)")
            A[k], A[j] = A[j], A[k]
            assignments += 3
            trace_logs.append(f"Масив після обміну: {A}")

            draw_heap(A, highlight=[k, j], sorted_part=n)

            k = j
            j = 2 * k + 1

    trace_logs.append("---------------------------------")


# --- heap_sort: реалізація + трасування + моделювання ---
def heap_sort(A):
    global comparisons, assignments

    n = len(A)
    trace = []
    realisation = []

    realisation.append(f"Початковий масив: {A}
")
    realisation.append("--- Фаза 1: Побудова максимальної купи ---")

    for i in range(n // 2 - 1, -1, -1):
        realisation.append(f"Занурюємо елемент з індексу {i}: {A[i]}")
        sink(A, i, n, trace, "build")
        draw_heap(A, sorted_part=n)

    realisation.append(f"Масив після побудови купи: {A}
")

    realisation.append("--- Фаза 2: Сортування ---")
    size = n

    while size > 1:
        realisation.append(f"Міняємо місцями корінь ({A[0]}) та останній елемент ({A[size-1]})")

        A[0], A[size - 1] = A[size - 1], A[0]
        assignments += 3

        draw_heap(A, highlight=[0, size-1], sorted_part=size)

        size -= 1
        realisation.append(f"Розмір купи зменшився до {size}. Відновлюємо властивості купи.")

        sink(A, 0, size, trace, "sort")
        draw_heap(A, sorted_part=size)

        realisation.append(f"Масив на поточному кроці: {A}")

    realisation.append(f"Відсортований масив: {A}")

    return realisation, trace


# --- Основна програма ---
while True:
    try:
        A = list(map(int, input("Введіть числа через кому: ").split(",")))
        break
    except ValueError:
        print("Помилка! Введіть лише числа через кому.")

print()

initial = A.copy()
realisation_logs, trace_logs = heap_sort(A)

print("
=== РЕАЛІЗАЦІЯ АЛГОРИТМУ ===")
for line in realisation_logs:
    print(line)

print("
=== ТРАСУВАННЯ АЛГОРИТМУ ===")
for line in trace_logs:
    print(line)

print("
=== МОДЕЛЮВАННЯ (кількісні показники) ===")
print(f"Кількість порівнянь: {comparisons}")
print(f"Кількість присвоєнь: {assignments}")

# Константа розміру таблиці
M = 13

# Список вхідних слів
WORDS = ["LUDYNA", "BEZ", "DRUZIV", "YAK", "DEREVO", "BEZ", "KORINNYA"]

# Словник позицій букв
LETTER_POSITIONS = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def simple_hash_from_map(key: str) -> int:
    """Хеш-функція: h(k) = (сума позицій букв) mod M"""
    sum_of_positions = sum(LETTER_POSITIONS.get(char, 0) for char in key)
    return sum_of_positions % M

def build_open_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з ланцюжками"""
    hash_table = [[] for _ in range(m)]
    for word in words:
        address = simple_hash_from_map(word)
        hash_table[address].append(word)
    return hash_table

def display_hash_table(table: list):
    print("\n--- Відкрита хеш-таблиця (M=13) ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання
hash_table = build_open_hash_table(WORDS, M)
display_hash_table(hash_table)

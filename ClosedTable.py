# Константа розміру таблиці
M = 13

# Список вхідних слів
WORDS = ["LUDYNA", "BEZ", "DRUZIV", "YAK", "DEREVO", "BEZ", "KORINNYA"]

LETTER_POSITIONS = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
    'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def primary_hash(key: str) -> int:
    """Первинна хеш-функція h(k) = (сума позицій букв) mod M"""
    return sum(LETTER_POSITIONS.get(c, 0) for c in key) % M

def build_closed_hash_table(words: list, m: int) -> list:
    """Будує хеш-таблицю з відкритою адресацією (лінійне дослідження)"""
    hash_table = [None] * m
    for word in words:
        start_address = primary_hash(word)
        for i in range(m):
            address = (start_address + i) % m
            if hash_table[address] is None:
                hash_table[address] = word
                break
    return hash_table

def display_hash_table(table: list):
    print("\n--- Закрита хеш-таблиця (Відкрита адресація, M=13) ---")
    print("Індекс | Слово")
    print("-------|----------------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")

# Виконання
hash_table = build_closed_hash_table(WORDS, M)
display_hash_table(hash_table)

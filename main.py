import random

def generate_array(length: int, min_val: int, max_val: int) -> list:
    """Генерує масив випадкових цілих чисел."""
    return [random.randint(min_val, max_val) for _ in range(length)]

def print_array(arr: list) -> None:
    """Виводить масив у форматі: {[cell - 0, value - 4], [cell - 1, value - 10]...}"""
    formatted_elements = [f"[cell - {i}, value - {v}]" for i, v in enumerate(arr)]
    print("{" + ", ".join(formatted_elements) + "}")

def bubble_sort(arr: list, ascending: bool = True) -> list:
    """
    Сортування бульбашкою.
    Якщо ascending=True — по зростанню, якщо False — по спаданню.
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Перевірка умови сортування залежно від напрямку
            should_swap = (a[j] > a[j + 1]) if ascending else (a[j] < a[j + 1])
            if should_swap:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def insertion_sort(arr: list, ascending: bool = True) -> list:
    """
    Сортування вставками.
    Якщо ascending=True — по зростанню, якщо False — по спаданню.
    """
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and ((a[j] > key) if ascending else (a[j] < key)):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def selection_sort(arr: list, ascending: bool = True) -> list:
    """
    Сортування вибором.
    Якщо ascending=True — по зростанню, якщо False — по спаданню.
    """
    a = arr.copy()
    n = len(a)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):

            if (a[j] < a[target_idx]) if ascending else (a[j] > a[target_idx]):
                target_idx = j
        a[i], a[target_idx] = a[target_idx], a[i]
    return a

if __name__ == "__main__":
    print("=== Генерація початкового масиву ===")
    initial_array = generate_array(length=8, min_val=1, max_val=20)
    print("Початковий масив:")
    print_array(initial_array)
    print("-" * 50)

    print("\n1. BUBBLE SORT (Сортування бульбашкою):")
    sorted_bubble_asc = bubble_sort(initial_array, True)
    print("Прямий порядок (True):")
    print_array(sorted_bubble_asc)

    sorted_bubble_desc = bubble_sort(initial_array, False)
    print("Зворотний порядок (False):")
    print_array(sorted_bubble_desc)

    print("\n2. INSERTION SORT (Сортування вставками):")
    sorted_insertion_asc = insertion_sort(initial_array, True)
    print("Прямий порядок (True):")
    print_array(sorted_insertion_asc)

    sorted_insertion_desc = insertion_sort(initial_array, False)
    print("Зворотний порядок (False):")
    print_array(sorted_insertion_desc)

    print("\n3. SELECTION SORT (Сортування вибором):")
    sorted_selection_asc = selection_sort(initial_array, True)
    print("Прямий порядок (True):")
    print_array(sorted_selection_asc)

    sorted_selection_desc = selection_sort(initial_array, False)
    print("Зворотний порядок (False):")
    print_array(sorted_selection_desc)
from collections import deque


def is_palindrome(s: str) -> bool:
    # Нормалізація даних
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())

    # Додавання рядка до двосторонньої черги
    char_deque = deque(cleaned_str)

    # Порівння символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Перевірка
print(is_palindrome("A man a plan a canal Panama"))  # Поверне True
print(is_palindrome("Hello"))  # Поверне False

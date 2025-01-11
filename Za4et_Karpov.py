def digit_to_num(char):
# Проверяемся является ли симвл числом
    if char.isdigit():
        return int(char)
    return None

def sum_of_digits_in_text(text):
 
    total_sum = 0
    # Проходимся по каждому символу из строки
    for char in text:
        num = digit_to_num(char)
        if num is not None:
            total_sum += num
    return total_sum

# Пример использования
text = "asjfhkasdjgh67asjkfhaskf3"
result = sum_of_digits_in_text(text)
print("Результат:", result)
"""Проверка знаний экранированных последовательностей."""

import time

from skillstest import SkillsTest


goodbye_message = "До новых встреч!"

# Запуск теста
while(1):
    result = SkillsTest.start()

    print("Ваш результат: ", result)

    print()
    answer = input("Хотите попробовать ещё раз? Да(y), Нет(любой другой символ): ")
    if(answer.lower() == 'y'):
        continue
    else:
        break

print()
print("\n", goodbye_message)

time.sleep(2)

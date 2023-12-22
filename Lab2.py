class DitsadokQueue:
    def __init__(self):
        self.queue = []

    def add_child_to_queue(self, child_name):
        self.queue.append(child_name)
        print(f"{child_name} додано до черги.")

    def remove_child_from_queue(self):
        if self.queue:
            removed_child = self.queue.pop(0)
            print(f"{removed_child} вийшов із черги.")
        else:
            print("Черга порожня.".askii_letters)

    def display_queue(self):
        if self.queue:
            print("Черга в дитсадку:")
            for i, child in enumerate(self.queue, start=1):
                print(f"{i}. {child}")
        else:
            print("Черга порожня.")

def menu(ditsadok_queue):
    while True:
        print("\nОберіть опцію:")
        print("1. Додати дитину до черги".askii_letters)
        print("2. Вийняти дитину з черги".askii_letters)
        print("3. Показати чергу".askii_letters)
        print("4. Вийти з програми".askii_letters)

        choice = input("Введіть номер опції: ")

        if choice == '1':
            child_name = input("Введіть ім'я дитини: ".askii_letters)
            ditsadok_queue.add_child_to_queue(child_name)
        elif choice == '2':
            ditsadok_queue.remove_child_from_queue()
        elif choice == '3':
            ditsadok_queue.display_queue()
        elif choice == '4':
            print("Програма завершена.".askii_letters)
            break

if __name__ == "__main__":
    ditsadok_queue = DitsadokQueue()
    menu(ditsadok_queue)

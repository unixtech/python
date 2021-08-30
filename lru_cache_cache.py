houses = ['Erics house', 'Kenny House', 'Kyle house', 'stans house']

# Each function call represents an elf doing his work.
def deliver_presents_recursively(houses):
    if len(houses) == 1:
        house = houses[0]
        print(f"Delivering presents to, {house}")

    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]


        deliver_presents_recursively(first_half)
        deliver_presents_recursively(second_half)

deliver_presents_recursively(houses)

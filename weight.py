container_weight = 0
container_count = 0
total_weight = 0
current_emptiness = 0
biggest_emptiness = 0
pack_number = 0

print("Podaj liczbę paczek do wysyłki.")
number_of_packs = int(input())

for load in range(number_of_packs):

    print("Podaj wagę elementu (min 1, max 10).")
    pack_weight = int(input())
    print("....................................")
    total_weight += pack_weight

    if pack_weight == 0:
        break
    elif pack_weight < 1 or pack_weight > 10:
        print("Błąd! Zła waga!")
        break
    elif 1 <= pack_weight <= 10:
        container_weight += pack_weight
        current_emptiness = 20 - container_weight
        print("najwieksza pustka: {}".format(biggest_emptiness))
    if container_weight > 20:
        container_count += 1
        if biggest_emptiness < 20 - (container_weight - pack_weight):
            biggest_emptiness = 20 - (container_weight - pack_weight)
            pack_number = container_count
        container_weight = 0
        container_weight += pack_weight
        print("petla > 20 {}".format(pack_weight))
        current_emptiness = 20 - container_weight
        print("petla >20: {}".format(biggest_emptiness))
    if container_weight < 20 and load == number_of_packs - 1:
        if biggest_emptiness < 20 - container_weight:
            biggest_emptiness = 20 - container_weight
            pack_number = container_count
        container_count += 1
        print("petla ostatnia: {}".format(biggest_emptiness))
    if container_weight == 20:
        container_count +=1
        container_weight = 0
        current_emptiness = 0
        print("petla == 20: {}".format(biggest_emptiness))

    print("bieżąca ilość wysłanych paczek {}".format(container_count))
    print("bieżąca waga kontenera {}".format(container_weight))
    print("bieżąca liczba kg: {}".format(total_weight))
    print("bieżąca liczba pustych kg: {}".format(current_emptiness))
    print("numer najbardziej pustej paczki: {}".format(pack_number))
    print("....................................")

pack_sent = f'Ilość wysłanych paczek: {container_count}'
kg_sent = f'Ilość wysłanych kilogramów: {total_weight}'
wasted_kg = f'Liczba pustych kilogramów: {container_count * 20 - total_weight}'
worst_pack_number = f'Numer najgorzej spakowanej paczki: {pack_number}'
worst_pack = f'Najwięcej pustych kilogramów na paczkę: {biggest_emptiness}'

if biggest_emptiness == 0:
    worst_pack_number = 'Numer najgorzej spakowanej paczki: brak'
    worst_pack = 'Najwięcej pustych kilogramów na paczkę: brak'
    wasted_kg = f'Liczba pustych kilogramów: brak'
if number_of_packs >=0:
    print(pack_sent)
    print(kg_sent)
    print(wasted_kg)
    print(worst_pack_number)
    print(worst_pack)
else:
    print("Błąd! Liczba paczek musi być dodatnia")

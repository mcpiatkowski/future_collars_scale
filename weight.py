container_weight = 0
container_count = 0
total_weight = 0
biggest_emptiness = 0
pack_number = 1  # Jedynka dla przypadku tylko jednej nie do końca załadowanej paczki

print("Podaj liczbę paczek do wysyłki.")
number_of_packs = int(input())

for load in range(number_of_packs):
    print("Podaj wagę elementu (min 1, max 10).")
    pack_weight = int(input())

# Obsługa błędów

    if pack_weight == 0 or pack_weight < 1 or pack_weight > 10:
        if container_weight > 0:
            container_count += 1
        if biggest_emptiness < 20 - container_weight and load > 0:
            biggest_emptiness = 20 - container_weight
            pack_number = container_count
        if pack_weight == 0:
            break
        else:
            print("Błąd! Zła waga!")
            break

# Właściwy program

    total_weight += pack_weight  # Dodane dopiero teraz, żeby nie dodawać błędnej wartości wagi do całości
    if 1 <= pack_weight <= 10:
        container_weight += pack_weight
    if container_weight > 20:
        container_count += 1
        if biggest_emptiness < 20 - (container_weight - pack_weight):
            biggest_emptiness = 20 - (container_weight - pack_weight)
            pack_number = container_count
        container_weight = 0
        container_weight += pack_weight
    if container_weight < 20 and load == number_of_packs - 1:
        container_count += 1
        if biggest_emptiness < 20 - container_weight:
            biggest_emptiness = 20 - container_weight
            pack_number = container_count
    if container_weight == 20:
        container_count += 1
        container_weight = 0

# Drukowanie

pack_sent = f'Ilość wysłanych paczek: {container_count}'
kg_sent = f'Ilość wysłanych kilogramów: {total_weight}'
wasted_kg = f'Liczba pustych kilogramów: {container_count * 20 - total_weight}'
worst_pack_number = f'Numer najgorzej spakowanej paczki: {pack_number}'
worst_pack = f'Najwięcej pustych kilogramów na paczkę: {biggest_emptiness}'

if biggest_emptiness == 0:  # Przypadek gdy paczki są idealnie zapakowane
    worst_pack_number = 'Numer najgorzej spakowanej paczki: brak'
    worst_pack = 'Najwięcej pustych kilogramów na paczkę: brak'
    wasted_kg = f'Liczba pustych kilogramów: brak'
if number_of_packs >= 0:
    print(pack_sent)
    print(kg_sent)
    print(wasted_kg)
    print(worst_pack_number)
    print(worst_pack)
else:
    print("Błąd! Liczba paczek musi być dodatnia")

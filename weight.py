container_weight = 0
container_count = 0
total_weight = 0

print("Podaj liczbę paczek do wysyłki.")
number_of_packs = int(input())

for load in range(number_of_packs):
    print("Podaj wagę elementu (min 1, max 10).")
    pack_weight = int(input())
    print("....................................")
    if pack_weight == 0:
        break
    if 1 <= pack_weight <= 10:
        container_weight += pack_weight
    if container_weight == 20:
        container_count +=1
    elif container_weight > 20:
        container_weight = 0
        container_weight += pack_weight
        container_count += 1
    total_weight += pack_weight
    print("aktualna waga kontenera {}".format(container_weight))
    print("aktualna liczba kg: {}".format(total_weight))
    print("....................................")

pack_sent = f'Ilość wysłanych paczek: {container_count}'
kg_sent = f'Ilość wysłanych kilogramów: {total_weight}'
wasted_kg = f'Liczba pustych kilogramów: {container_count * 20 - total_weight}'

print(pack_sent)
print(kg_sent)
print(wasted_kg)


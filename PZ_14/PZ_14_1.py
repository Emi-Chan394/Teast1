#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом файле.

# Открываем исходный файл и два выходных файла
with open('ip_address.txt', 'r', encoding='utf-8') as source_file, \
     open('file1.txt', 'w', encoding='utf-8') as file1, \
     open('file2.txt', 'w', encoding='utf-8') as file2:

    count_file1 = 0
    count_file2 = 0

    for line in source_file:
        line = line.strip()
        if not line:
            continue

        # Предполагаем, что в строке содержится IP-адрес в формате a.b.c.d
        parts = line.split()
        ip_found = False
        for part in parts:
            octets = part.split('.')
            if len(octets) == 4 and all(o.isdigit() for o in octets):
                first_octet = int(octets[0])
                second_octet = int(octets[1])
                ip_found = True
                break

        if ip_found:
            if first_octet != 0 and second_octet != 0:
                file1.write(line + '\n')
                count_file1 += 1
            else:
                file2.write(line + '\n')
                count_file2 += 1
        else:
            # если IP не найден, можно решить, что делать — например, в file2
            file2.write(line + '\n')
            count_file2 += 1

print(f'Количество строк в первом файле: {count_file1}')
print(f'Количество строк во втором файле: {count_file2}')
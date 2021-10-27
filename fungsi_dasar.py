# TODO:
# 1. len (udah)
# 2. append (udah)
# 3. remove (udah)
# 4. startswith ()

def startswith(string_yang_dicek, karakter_yang_dicek):
    return True if string_yang_dicek[0] == karakter_yang_dicek else False

def length(list):
    count = 0
    for items in list:
        count += 1
    return count

# Cara penggunaan length(list):
# sama dengan len(list)

def append(list_lama, item_baru):
    new_list = ['*' for i in range(length(list_lama) + 1)]

    for i in range(length(list_lama)):
        new_list[i] = list_lama[i]
    new_list[length(list_lama)] = item_baru

    list_lama = new_list
    return list_lama

# Cara penggunaan append(list_lama, item_baru):
# test_list = ['p', 'q']
# test_list = append(test_list, 'r')
# print(test_list)

def remove(list_lama, item_yang_di_remove):
    item_ketemu = False
    while item_ketemu == False:
        for i in reversed(range(length(list_lama))): # Catatan, ini pakai reversed, kalau ga pakai ntar ga mirip sama fungsi remove bawaan python.
            if list_lama[i] == item_yang_di_remove:
                index_yang_di_remove = i
                item_ketemu = True
    list_baru = []
    for j in range(length(list_lama)):
        if j != index_yang_di_remove:
            list_baru = append(list_baru, list_lama[j])
        else:
            pass
    return list_baru

# Cara penggunaan remove(list_lama, item_yang_di_remove)
# test_list = ['p','q','p', 's', 'p']
# test_list = remove(test_list, 'p')
# print(test_list)
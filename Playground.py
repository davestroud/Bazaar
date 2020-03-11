peopleKeys, peopleValues = [], []
lastKey = 0
for k1, v1 in people.items():
    row = []

    for k2, v2 in v1.items():
        peopleKeys.append(k1+'_'+k2)
        if k1 == lastKey:
            row.append(v2)
            lastKey = k1

        else:
            peopleValues.append(row)
            row.append(v2)
            lastKey(k1)



restaurantKeys, restaurantValues = [], []
for k1, v1 in restaurants.items():
    for k2, v2 in v1.items():
        restaurantKeys.append(k1+'_'_+k2)
        restaurantValues.append(v2)
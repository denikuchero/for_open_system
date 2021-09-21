from statistics import median

dataset = {'admin$': 2, 'Borat': 18, 'daemon_': 6,
           'Kovalev': 16, 'Anderson': 21, 'Corvin': 3,
           'aBrams': 14, '13': 20, 'Gerhaгd': 19, 'Zidane': 12,
           'Messi': 10, 'Rupert': 10}


footballers = ['Messi', 'Zidane']

# -------------------------------------------------------------------------------------
# 1) Нам нужны только люди (фамилия состоит из букв)
def onli_man(dataset):
    dataset_for_men = {}
    for item in dataset.keys():
        if item.isalpha():
            dataset_for_men[item] = dataset[item]
    return dataset_for_men


# -------------------------------------------------------------------------------------
# 2) Нам не нужны футболисты
def without_footbals(dataset):
    dataset_without_footbals = {}
    for item in dataset.keys():
        if item not in footballers:
            dataset_without_footbals[item] = dataset[item]
    return dataset_without_footbals


# -------------------------------------------------------------------------------------
# 3) Показатель может быть только чётным, остальное – искажения. Искажения исправить: привести к ближайшему меньшему чётному.
def chet_result(dataset):
    new_dataset = {}
    for item in dataset.keys():
        if int(dataset[item] % 2 ) == 0:
            new_dataset[item] = dataset[item]
        else:
            new_dataset[item] = dataset[item] - 1

    return new_dataset


# -------------------------------------------------------------------------------------
# шаг 2
# Надо вернуть список фамилий тех, у кого значение показателя выше медианного, в порядке убывания показателя.
def result_list_famili_gt_median(dataset):
    list_median = []
    result = []
    invert_dataset = {}

    for item in dataset.keys():
        invert_dataset[dataset[item]] = item
        list_median.append(int(dataset[item]))

    median_dict = median(list_median)
    list_median.sort(reverse=True)

    for index, item in enumerate(list_median):
        if item < median_dict:
            del list_median[index:]
            break

    for item in list_median:
        result.append(invert_dataset[item])

    return result


if __name__ == '__main__':
    print('1) Нам нужны только люди (фамилия состоит из букв):' , onli_man(dataset))
    print('2) Нам не нужны футболисты:', without_footbals(dataset))
    print('3) Показатель может быть только чётным, остальное – искажения:',chet_result(dataset))

    result = result_list_famili_gt_median(dataset)
    print('Cписок фамилий тех, у кого значение показателя выше медианного, в порядке убывания показателя:',result)

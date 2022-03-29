# complexity -->> O(n)
def find_transaction(trans, search):
    for idx, value in enumerate(trans):
        if value['id'] == search:
            return idx
    return -1

trans = [{
    'name': 'Subhendu',
    'id': '123',
    'pay': 3000
},
    {
        'name': 'ardhendu',
        'id': '124',
        'pay': 5000
    }
]
id_search = '124'
print(find_transaction(trans, id_search))
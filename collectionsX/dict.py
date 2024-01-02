# DICTIONARY

# Define Dict.

d1 = {}
d2 = dict()


d2['k1'] = 'v1'  # adds entry 's': 3

d3 = {
    'k1': 'value1',
    'k2': 'value2',
    'k3': 'value3',
}
d4 = dict(k1='value1', k2='value2', k3='value3')
print(d3['k1'])  # value1


# dictionary keys must be immutable (strings, numbers, tuples)



del dict['k1']  # {'k2': 'value2', 'k3': 'value3'}
dict['k3'] = 'new_value3'  # {'k2': 'value2', 'k3': 'new_value3'}
len(dict)  # 2
dict.get("k3")  # new_value3

dict_keys = dict.keys()  # dict_keys(['k3', 'k2'])
dict.values()  # dict_values(['new_value3', 'value2'])
dict.items()  # dict_items([('k3', 'new_value3'), ('k2', 'value2')])

'k2' in dict  # True
'value2' in dict  # False , does not work with 'values'
for _ in dict: print(_)  # k2 \n k3


def bool():
    '''

    :return: property as dictionary
    '''
    return {
        'name'    : 'on',
        'value'   : False,
        'metadata': {
            'label'   : 'On/Off',
            'type'    : 'boolean',
            '_type'   : 'BooleanProperty',
            'readOnly': True,
            },
        }



binarySensor = {
    'type'      : 'binarySensor',
    '_context'  : 'https://iot.mozilla.org/schemas',
    '_type'     : ['BinarySensor'],
    'name'      : 'Virtual Binary Sensor',
    'properties': [bool(), ],
    'actions'   : [],
    'events'    : [],
    }

print('BINARY SENSOR PROPERTIES:')
print(binarySensor['properties'])

for property in binarySensor['properties']:
    print('a')

for property in binarySensor['events']:
    print('b')

VIRTUAL_THINGS = [
    binarySensor
    ]

for dev in VIRTUAL_THINGS:
    print('DEV:')
    print(dev)

for dev in VIRTUAL_THINGS[0]:
    print('DEV[0]:')
    print(dev)

print(binarySensor['type'])


def extract_from_dict_1(**params: dict):
    """
    params = {'k2': 'value2', 'k3': 'value3', 'k1': 'value1'}
    extract_from_dict_1(**params)
    equiv to
    extract_from_dict_1( k2= 'value2' , k3 ='value3' , k1 = 'value1' )
    :param params:
    :return:
    """

    return 0


def extract_from_dict(*args, **kwargs):
    '''
    # {'k2': 'value2', 'k3': 'value3', 'k1': 'value1'}
    :param args:
    :param kwargs:
    :return:
    '''
    pass


# todo https://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/


# extract_from_dict_1(dict)


abb = {1: '3'}
print(abb)
abb.update({1: '4'})
print(abb)

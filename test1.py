from gateway_addon.property import Property


#adapter = Adapter('test_id', 'test_package', verbose=True)
#device = Device(adapter,"id123")

descripton_1 = {
    'label' : 'description_1'
}
property1 = Property( None,'property1', descripton_1)

descripton_2 = {
    'label' : 'description_2'
}
property2 = Property( None,'property2', descripton_2)


properties = {}
properties['property1'] = property1
properties['property2'] = property2

properties_transformed = {k: v.as_dict() for k, v in properties.items()}



print('# property1')
print(property1)
print('# properties')
print(properties)
print('# properties_transformed')
print(properties_transformed)
print('# properties.get(\'property1\', None)')
print(properties.get('property1', None))
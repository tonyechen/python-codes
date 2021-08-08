# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}
#print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(type(capitals.values()))
capitals.update({'USA':'Los Angeles'})
capitals.pop("China")
capitals.clear()

for key,value in capitals.items():
    print(key,value)


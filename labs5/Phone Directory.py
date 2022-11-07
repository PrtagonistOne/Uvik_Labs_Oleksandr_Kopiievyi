

phone_directory = open('phone_directory.txt', 'r').read().split('\\n')
potential_persons = [phone.split() for phone in phone_directory]


phone_number_limit = 14
for persons in potential_persons:
    phone_number = ''
    name = ''
    address = ''
    for person_info in persons:
        if person_info.count('-') == 3:
            phone_number = ''.join(f'{num[-1]}-' if count == 0 else f'{num}-' for count, num in enumerate(person_info.split('-')))[:phone_number_limit]
        elif any(['<' in person_info, '>' in person_info]):
            name += f'{person_info} '
    for x in persons:
        if phone_number in x:
            persons.remove(x)
    try:
        persons.remove(name.split()[0])
        persons.remove(name.split()[1])
        for let in persons:
            address += f'{let} '
        if all([phone_number, name, address]):
            print(f'Phone => {phone_number}, Name => {name.strip()[1:-2]}, Address => {address}')
        elif not phone_number:
            print('Error => Not found: num')
        elif not address:
            print('Error => Not found: address')
    except IndexError:
        print('Error => Not found: name')


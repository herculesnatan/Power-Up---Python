def bulid_person(first_name, last_name, age=None):
    # Return a dictionary of information about about a person.
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = bulid_person('jimi', 'hendrix')
print(musician)

musician = bulid_person('hercules', 'natan', 22)
print(musician)
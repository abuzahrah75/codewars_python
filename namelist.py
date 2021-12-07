def namelist(names):
    if len(names) == 0:
        return ""
    else:
        if len(names) > 2:
            return ", ".join(map(lambda name: name['name'], names[:-2])) + \
                ", " + names[-2:][0]['name'] + \
                " & " + names[-2:][1]['name']
        else:
            return names[0]['name'] if len(names) < 2 else names[0]['name'] + " & " + names[1]['name']


# from best result
# def namelist(names):
#     if len(names) > 1:
#         return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
#                                 names[-1]['name'])
#     elif names:
#         return names[0]['name']
#     else:
#         return ''
print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# returns 'Bart, Lisa & Maggie'

print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# returns 'Bart & Lisa'

print(namelist([{'name': 'Bart'}]))
# returns 'Bart'

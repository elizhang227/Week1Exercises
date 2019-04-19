name = input('Please provide a name: ')
verb = input('Pleae provide a verb: ')
adj = input('Pleae provide an adverb: ')

def capitalize(name):
    capitalized = name.capitalize()
    return capitalized

def madlibs(name, verb, adj):
    fixed_name = capitalize(name)
    return print('%s likes to %s %s' % (fixed_name, verb, adj))

madlibs(name, verb, adj)

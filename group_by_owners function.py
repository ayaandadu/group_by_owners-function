files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}


def group_by_owners(files):
    ownerdict = {}
    for file, owner in files.items():
        if owner in ownerdict:
            ownerdict[owner].append(file)
        else:
            ownerdict[owner] = [file]
    return ownerdict


print(group_by_owners(files))

# OUTPUT:-
# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}
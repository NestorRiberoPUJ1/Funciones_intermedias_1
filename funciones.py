x = [[5, 2, 3], [10, 8, 9]]
estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
directorio_deportes = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

x[1][0] = 15
estudiantes[0]['last_name'] = "Bryant"
directorio_deportes["fútbol"][0] = "Andrés"
z[0]['y'] = 30


def iterateDictionary(studentList):
    for x in studentList:
        format = ""
        for y in x:
            format += y+" - "+x[y]
            if(y == "first_name"):
                format += ", "
        print(format)


def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])


estudiantes = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
#iterateDictionary(estudiantes)
#iterateDictionary2("first_name", estudiantes)

def printInfo(dictionary):
    for x in dictionary:
        print(f"{len(dictionary[x])} {x.upper()}")
        for y in dictionary[x]:
            print(y)
        print("")

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

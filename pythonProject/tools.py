import requests

def getNumId(lista, values):
    for r in values['response']['groups']:
        if r['id'] not in lista:
            lista.append(r['id'])
    return lista

def getData(id):
    response = requests.get(
        "https://mfwkweb-api.clarovideo.net/services/content/data?device_id=web&device_category=web&device_model=web&device_type=web&device_so=Chrome&format=json&device_manufacturer=generic&authpn=webclient&authpt=tfg1h3j4k6fd7&api_version=v5.92&region=argentina&HKS=f9p95s8eo8mjmt4oe80fc7u9r4&group_id="+str(id))
    return formatData( response.json())

def formatData(values):
    array = {}
    array['titulo'] = getTitle(values)
    array["anio"] = getYear(values)
    array["tipo"] = "Pelicula"
    array["genero"] = getGenre(values)
    array["descripcion"] = getDescription(values)
    array["actores"] = getCast(values)
    array["director"] = getDirector(values)
    array["plan"] = getPlan(values)
    return array

def getTitle(values):
    common = values['response']['group']['common']
    return common['title']

def getYear(values):
    return values['response']['group']['common']['extendedcommon']['media']['publishyear']

def getGenre(values):
    returnGenres = ""
    genres = values['response']['group']['common']['extendedcommon']['genres']['genre']
    for e in genres:
        returnGenres += e['desc']
        returnGenres += ", "
    returnGenres = returnGenres[:-2]
    return(returnGenres)

def getDescription(values):
    return values['response']['group']['common']['description']

def getCast(values):
    dataCast = values['response']['group']['common']['extendedcommon']['roles']['role']
    separetedCast = ""
    for e in dataCast:
        if e['id'] == '13617516':
            separetedCast = e['talents']['talent']
            break
    cast = ""
    for e in separetedCast:
        cast += e['fullname']
        cast += "; "
    cast = cast[:-2]
    return(cast)

def getDirector(values):
    dataDirector = values['response']['group']['common']['extendedcommon']['roles']['role']
    directors = ""
    for e in dataDirector:
        if e['id'] == '13617517':
            directors = e['talents']['talent']
            break
    direction = ""
    for e in directors:
        direction += e['fullname']
        direction += "; "
    direction = direction[:-2]
    return(direction)

def getPlan(values):
    tipos = values['response']['group']['common']['extendedcommon']['format']
    return(tipos['types'])

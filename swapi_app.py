import requests

# requests Module enthalt sich Exception Methode
# versuch in der Funktion requests.get() timeout = 3


class Person:
    def __init__(self, name, groesse, gewicht, haarfarbe) -> None:
        self.name = name
        self.groesse = groesse
        self.gewicht = gewicht
        self.haarfarbe = haarfarbe

    def __str__(self):
        return f"Name: {self.name} \t\t Grösse: {self.groesse} \t\t Gewicht: {self.gewicht} \t\t Haarfarbe: {self.haarfarbe}"


def getSWPeople(url: str):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print('Status Code :', response.status_code)
        data = response.json()
        return [data["results"], data["next"]]  # return peoples in results

    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)


def extractSWPeople(url):
    persons: Person = []

    while url:
        peoples, url = getSWPeople(url)

        # print(f"People's keys: {peoples[0].keys()} \n")
        # print all the people element
        for p in peoples:
            person = Person(p['name'], p['height'], p['mass'], p['hair_color'])
            persons.append(person)
            # print(f"Name: {p['name']}")
            # print(person)
    return persons


# Extract all people
url = "https://swapi.dev/api/people"
persons = extractSWPeople(url)
print(len(persons))
for person in persons:
    print(person)

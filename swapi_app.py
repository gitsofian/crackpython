from cgitb import text
import requests


class RequestExeption(Exception):
    def __str__(self):
        print(f"Problem occur! Check the Error!")


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
        response = requests.get(url, timeout=3)
        response.raise_for_status()

        print('Status Code :', response.status_code)

        data = response.json()
        print(f"data keys: {data.keys()} \n")
        print(f"count: {data['count']} \n")
        print(f"count: {data['next']} \n")
        print(f"count: {data['previous']} \n")

        peoples = data["results"]
        print()
        print(f"People's keys: {peoples[0].keys()} \n")

        persons = []
        # print all the people element
        for p in peoples:
            person = Person(p['name'], p['height'], p['mass'], p['hair_color'])
            persons.append(person)
            # print(f"Name: {p['name']}")
            print(person)

        # check the next page link
        next_url = data['next']
        if not next_url:
            return -1
        else:
            return next_url

    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.RequestException as e:
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)


url = "https://swapi.dev/api/people/s"
url = print(getSWPeople(url))

'''
ctrl = True     # control variable
while(ctrl):
    resp = print(getSWPeople(url))
    if resp == -1:
        print('No People enough!')
        ctrl = False
    else:
        print(f"next url: {resp}")
        url = resp
'''

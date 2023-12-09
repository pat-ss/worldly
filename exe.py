import json
import random

def generate_random(list):
    num = list.index(random.choice(list))
    return(num)

def main():

    with open('world_countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)

    country = countries[generate_random(countries)]
    #country = {}
    #for c in countries:
    #    if c['name'] == "England":
    #        country = c
    num_keys = len(country.keys())
    random_key = random.randrange(4, 14)
    #random_key = 4
    if random_key == 4:
        if len(country['tld']) == 1:
            x = input("What is the top level domain (what comes after www.something.) of " + country['name'] + "? ")
            if x.lower() == country['tld'][0] or ("." + x.lower()) == country['tld'][0]:
                print("Correct!")
            else:
                print("Oops, that's wrong...")
            main()
        else:
            x = input(country['name'] + " has " + str(len(country['tld'])) + " possible top level domains (what comes after www.something.). What are they? ")
            x = x.replace(", ", "")
            x = x.replace(",", " ")
            split_x = x.split()
            tld = []
            for i in country['tld']:
                tld.append(i)
            counter = 0
            for i in split_x:
                if i.lower() in tld or ("." + i.lower()) in tld:
                    counter = counter + 1
                    i = i.replace(".", "")
                    i = "." + i
                    tld.remove(i)
            if counter == 0:
                print("Not even one right...")
            elif counter < len(country['tld']) and counter != 0:
                print("You got " + str(counter) + " right, not bad...")
            else:
                print("You got them all right, who would've thought...")
            main()
    elif random_key == 5:
        x = input("Is " + country['name'] + " a member of the United Nations? ")
        main()
    elif random_key == 6:
        x = input("Is " + country['name'] + " landlocked? ")
        main()
    elif random_key == 7:
        currencies_codes = []
        currencies_names = []
        for currency_code, currency_details in country['currencies'].items():
            currencies_codes.append(currency_code.lower())
            currencies_names.append(currency_details['name'].lower())
            if len(currencies_codes) == 1:
                x = input(country['name'] + " has one currency. What is it? ")
                main()
            else:
                x = input(country['name'] + " has " + str(len(currencies_codes)) + " currencies. What are they? ")
                main()
    elif random_key == 8:
        if len(country['capital']) == 1:
            x = input("What is the capital of " + country['name'] + "? ")
            main()
        else:
            x = input(country['name'] + " has " + str(len(country['capital'])) + " capitals. What are they? ")
            main()
    elif random_key == 9:
        x = input("In which continent is " + country['name'] + " located at? ")
        main()
    elif random_key == 10:
        x = input("In which subregion is " + country['name'] + " located at? ")
        main()
    elif random_key == 11:
        languages = []
        for language_code, language_name in country['languages'].items():
            languages.append(language_name)
        if len(languages) == 1:
            x = input("Citizens of " + country['name'] + " speak one language. Which language is it? ")
            main()
        else:
            x = input("Citizens of " + country['name'] + " speak " + str(len(languages)) + " languages. What languages are they? ")
            main()
    elif random_key == 12:
        if 'borders' in country:
            if len(country['borders']) == 1:
                x = input(country['name'] + " is bordered by one country. Which country it is? ")
                main()
            else:
                x = input(country['name'] + " is bordered by " + str(len(country['borders'])) + " countries. What countries are they? ")
                main()
        else:
            main()
    elif random_key == 13:
        ops = [1, 2]
        op = generate_random(ops)
        if op == 1:
            if len(country['car']['signs']) == 1:
                x = input("What country code appears on " + country['name'] + "'s license plates? ")
                main()
            else:
                x = input("In " + country['name'] + ", there are " + str(len(country['car']['signs'])) + " country codes that can appear on their license plates. What codes are they? ")
                main()
        else:
            x = input("On which side of the road do " + country['name'] + "'s citizens drive? ")
            main()
    else:
        print("error, please reboot")


        



main()


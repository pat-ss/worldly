import json
import random

def generate_random(list):
    num = list.index(random.choice(list))
    return(num)

def main():

    with open('world_countries.json', 'r', encoding='utf-8') as file:
        countries = json.load(file)

    country = countries[generate_random(countries)]
    country = {}
    #for c in countries:
        #if c['name'] == "Russia":
            #country = c
    num_keys = len(country.keys())
    random_key = random.randrange(4, 10)
    #random_key = 9
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
        x_bool = None
        while True:
            
            x = input("Is " + country['name'] + " a member of the United Nations? ")
            if x.lower() == "y" or x.lower() == "yes" or x.lower() == "s" or x.lower() == "sim":
                x_bool = True
            elif x.lower() == "n" or x.lower() == "no" or x.lower() == "nao" or x.lower() == "não":
                x_bool = False
            else:
                print("Input not valid")
                continue
            if x_bool == None:
                break
            else:
                if x_bool == country['unMember']:
                    print("Correct!")
                    main()
                else:
                    print("Oops, that's wrong...")
                    main()     
    elif random_key == 6:
        
        x_bool = None
        while True:
            
            x = input("Is " + country['name'] + " landlocked? ")
            if x.lower() == "y" or x.lower() == "yes" or x.lower() == "s" or x.lower() == "sim":
                x_bool = True
            elif x.lower() == "n" or x.lower() == "no" or x.lower() == "nao" or x.lower() == "não":
                x_bool = False
            else:
                print("Input not valid")
                continue
            if x_bool == None:
                break
            else:
                if x_bool == country['landlocked']:
                    print("Correct!")
                    main()
                else:
                    print("Oops, that's wrong...")
                    main()
    elif random_key == 7:
        currencies_codes = []
        currencies_names = []
        counter = 0
        for currency_code, currency_details in country['currencies'].items():
            currencies_codes.append(currency_code.lower())
            currencies_names.append(currency_details['name'].lower())
        if len(currencies_codes) == 1:
            x = input(country['name'] + " has one currency. What is it? ")
            if x.lower() == currencies_codes[0].lower() or x.lower() == currencies_names[0].lower():
                print("Correct!")
                main()
            else:
                print("Uuuhhh, that's wrong...")
                main()
        else:
            x = input(country['name'] + " has " + str(len(currencies_codes)) + " currencies. What are they? ")
            duplicate_codes = currencies_codes
            currency_counter = len(duplicate_codes)
            x_arr = x.split(",")
            for x2 in x_arr:
                x2 = x2.replace(",", "").lower()
                if x2[0] == " ":
                    x2 = x2[1:]
                if x2 in currencies_codes or x2 in currencies_names:
                    counter += 1
                    if x2 in currencies_codes:
                        currencies_codes.remove(x2)
                    elif x2 in currencies_names:
                        currencies_names.remove(x2)
            if counter == 0:
                print("Not even one right...")
                main()
            elif counter > 0 and counter < currency_counter:
                print("You got " + str(counter) + " right. Not bad...")
                main()
            else:
                print("Wow, I can't believe you got them all right...")
                main()
    elif random_key == 8:
        if len(country['capital']) == 1:
            x = input("What is the capital of " + country['name'] + "? ")
            main()
        else:
            x = input(country['name'] + " has " + str(len(country['capital'])) + " capitals. What are they? ")
            main()
    elif random_key == 9:
        if len(country['continents']) == 1:
            x = input("In which continent is " + country['name'] + " located at? ")
            if x.lower() == country['continents'][0].lower():
                print("Correct!")
                main()
            else:
                print("Oops, not this time...")
                main()
        else:
            x = input(country['name'] + " is located in " + str(len(country['continents'])) + " continents. What are they? ")
            x_arr = x.split(",")
            continents = country['continents']
            counter = 0
            for x2 in x_arr:
                x2 = x2.lower()
                if x2[0] == " ":
                    x2 = x2[1:]
                for continent in continents:
                    continent = continent.lower()
                    if x2 == continent:
                        counter += 1
                        del(continents[continents.indexOf(continent)])
            if counter == 0:
                print("Not even one right...")
            elif counter > 0 and counter < len(country['continents']):
                print(str(counter) + " right, not bad...")
            else:
                print("All correct? Nice!")
                           
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


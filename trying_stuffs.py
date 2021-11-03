import csv, os, time, functools
from models import NearEarthObject
# from workspace.models import NearEarthObject


def timefunc(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        func = function(*args, **kwargs)
        end = time.time()
        print(f"{end - start} seconds for '{function.__name__}'")
        return func
    return wrapper

def memoize(function):
    function._cashe = {}
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        key = (function.__name__, args, tuple(kwargs.items()))
        if key not in function._cashe:
            function._cashe[key] = function(*args, **kwargs)
        return function._cashe[key]
    return wrapper

def some_csv_reading():
    counter = 0
    neos_lst = []
    with open('data/neos.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if counter == 10:
                break
            # print(f"pdes: {row['pdes']}; name: {row['name']}; pha: {row['pha']}; diameter: {row['diameter']}.")
            counter += 1
            neos_lst.append(NearEarthObject(row['pdes'], row['name'], row['diameter'], row['pha']))
            # neos_lst.append(NearEarthObject({row['pdes']}, {row['name']}, {row['diameter']}, {row['pha']}))

    for neo in neos_lst:
        print(neo)

if __name__ == '__main__':

    print(os.getcwd())

    # i = "Roll for initiative!"
    # with open('data/i.pickle', 'wb') as f:
    #     pickle.dump(i, f)
    # with open('data/i.pickle', 'rb') as f:
    #     print(pickle.load(f))

    '''
        73P-BT Schwassmann-Wachmann
        79P du Toit-Hartley
        85P Boethin
        96P Machholz
        103P Hartley
        104P Kowal
        109P Swift-Tuttle
        122P de Vico
        141P Machholz
        141P-A Machholz
        141P-D Machholz
        161P Hartley-IRAS
        162P Siding Spring
        169P NEAT
        177P Barnard
        181P Shoemaker-Levy
        182P LONEOS
        185P Petriew
        189P NEAT
        197P LINEAR
        206P Barnard-Boattini
        207P NEAT
        209P LINEAR
        210P Christensen
        217P LINEAR
        222P LINEAR
        249P LINEAR
        252P LINEAR
        255P Levy
        262P McNaught-Russell
        263P Gibbs
        273P Pons-Gambart
        289P Blanpain
        294P LINEAR
        300P Catalina
        306P LINEAR
        317P WISE
        319P Catalina-McNaught
        320P McNaught
        321P SOHO
        322P SOHO
        323P SOHO
        325P Yang-Gao
        333P LINEAR
        342P SOHO
        364P PANSTARRS
        384P Kowalski
        387P Boattini
        1766 G1 Helfenzrieder
        1770 L1 Lexell
        1884 O1 Barnard
        1894 F1 Denning
        1895 Q1 Swift
        1917 F1 Mellish
        1921 H1 Dubiago
        1937 D1 Wilk
        1942 EA Vaisala
        1978 R1 Haneda-Campos
        1989 A3 Bradfield
        1991 L3 Levy
        1999 J6 SOHO
        1999 RO28 LONEOS
        2001 OG108 LONEOS
        2001 W2 BATTERS
        2002 R5 SOHO
        2002 S7 SOHO
        2003 T12 SOHO
        2005 T4 SWAN
        2006 HR30 Siding Spring
        2007 T2 Kowalski
        2008 Y12 SOHO
        2009 WX51 Catalina
        2010 L5 WISE
        2011 NO1 Elenin
        2011 S2 Kowalski
        2012 NJ La Sagra
        2013 TL117 Lemmon
        2015 A3 PANSTARRS
        2015 D1 SOHO
        2015 F5 SWAN-Xingming
        2015 X8 NEOWISE
        2016 BA14 PANSTARRS
        2016 J3 STEREO
        2017 Y3 Leonard
        2019 M2 ATLAS
        2019 Y3 Catalina
        2019 Y4-D ATLAS
        2020 G1 Pimentel
        2020 M3 ATLAS
        2020 P4-B
        2020 P4-C
    '''

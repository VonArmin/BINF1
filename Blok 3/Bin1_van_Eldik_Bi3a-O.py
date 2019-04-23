# auteur  : Armin van Eldik
# nummer  : 618604
# DOC     : 10-04-2019
# opdracht: Bi3a-O
# klas    : BIN-1A
# functie : informatica toets Bi3a-O
import mysql.connector


# connectie heb ik global gemaakt zodat je het niet 100x hoeft door te geven in andere functies
connection = mysql.connector.connect(host='ensembldb.ensembl.org',
                                     user='anonymous',
                                     db='ensembl_production_95')


def main():
    while True:
        filter = input('Waar wil je op zoeken? : ')
        if filter == '':
            print('je moet wel iets invoeren')
        else:
            filter_db(filter)
        if input('nog een? y/n: ') == 'n':
            connection.close()
            break


def filter_db(filter):
    """filtert de biologische database dmv een sql query en een filter ingeveoerd door gebruiker
    :param filter: filter ingevoerd door gebruiker
    :return: roept printer aan wanneer er iets gevonden is zo niet wordt dat geprint
    """
    cursor = connection.cursor()
    cursor.execute(
        "select common_name, web_name, scientific_name from species "
        "where (common_name regexp '{}') or (scientific_name regexp '{}');".format(filter, filter)
    )
    rows = cursor.fetchall()
    if rows:
        print('aantal hits : ', len(rows))
        for row in rows:
            printer(row)
    else:
        print('niets gevonden')
    cursor.close()
# cursor wordt aangemaakt waarna uitgevoerd
# rows = opslagplaats voor cursor
# als er iets gevonden is wordt de printer functie aangeroepen
# cursor wordt gesloten


def printer(row):
    """ deze functie print alle gegevens die gevonden zijn(worden)
    zodra de functie aangeroepen wordt, wordt de get_alias functie aangeroepen, er is dus al een hit
    :param row: lijst van (common name, web_name, scientific_name)
    :return: print van alle info die gevonden is
    """
    alias_list = get_aliases(row[1])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
          '\ncommon name: {}'
          '\nscientific name : {}'
          '\naliases : {}'
          .format(row[0], row[2], alias_list))
# er wordt een lijst aangemaakt waar alle aliasen in staan
# de gegevens worden geprint


def get_aliases(common_name):
    """deze functie wordt aangeroepen door printer en vind bij de common name de aliassen
    :param common_name: common name gevonden door filter_db
    :return: een lijst van de aliassen voor het desbetreffende organisme
    """
    alias_list = []
    cursor = connection.cursor()
    cursor.execute(
        "select alias "
        "from species_alias join species using(species_id) "
        "where common_name regexp '{}'".format(common_name)
    )
    aliases = cursor.fetchall()
    for name in aliases:
        for alias in name:
            alias_list.append(alias)
    cursor.close()
    return alias_list
# alias_list een lijst waarin de aliassen opgeslagen worden
# cursor wordt aangemaakt waarna uitgevoerd
# de lijst wordt gevuld vanuit de cursor
# cursor wordt geclosed en de lijst geretourneerd


main()

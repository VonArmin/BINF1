#maak een variable voor boterham
#maak een variable voor pindakaas
#tel de variabelen op

var1 = 'boterham'
var2 = 'pindakaas'

print ('je hebt een ', var1,'met', var2)

#maak een variabele voor Boterham
#maak een variabele voor pindkaas
#maak een variabele voor hagelslag
#tel de variabelen op

var3 = 'hagelslag'
print ('je hebt een ', var1, 'met', var2, 'en', var3)


# (Regels: deelbaar door 4, maar niet door 100, wel door 400)
# variable met user input met het jaartal, converteer naar integer
# als jaar modulo 4 nul is
#   als jaar modulo 100 nul is
#       als jaar module 400 nul is
#           geef weer dat het een schrikkeljaar is
#       anders
#           geef weer dat het geen schrikkeljaar is
#   anders
#       geef weer dat het een schrikkeljaar is
# anders
#   geef weer dat het geen schrikkeljaar is


#vraag om input: zegt het waf of miauw?
#als input gelijk is aan waf print: het is een hond
#als input gelijk is aan miauw print: het is een kat
#anders vraag om input heeft het vleugels of vinnen?
#als input gelijk is aan vleugels print: het is een vogel
#als input gelijk is aan vinnen print: het is een vis

kathond = input('zegt het waf of miauw?')
if kathond == 'waf' :
    print ('het is een hond')
elif kathond == 'miauw' :
    print ('het is een kat')
else :
    vogelvis = input ('heeft het vleugels of vinnen?')
    if vogelvis == 'vleugels' :
        print ('het is een vogel')
    if vogelvis == 'vinnen' :
        print ('het is een vis')

#open file als sequentie
#tel aantal ACTG etc.
#als totaal == actg dan is het dna anders is het een eiwit
#als het DNA is print totaal aantal actg
        


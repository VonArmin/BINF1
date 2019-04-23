# demo

import mysql.connector

verbinding =  mysql.connector.connect(host='ensembldb.ensembl.org',
                                      user='anonymous',
                                      db='homo_sapiens_core_95_38')

cursor = verbinding.cursor()
cursor.execute(
    'select * '
    'from gene '
    'limit 10'
)

row = cursor.fetchall()
for line in row:
    print(line)
cursor.close()
verbinding.close()
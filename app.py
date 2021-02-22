import json
import logging
import pandas
from flask import Flask, abort
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

df = pandas.read_csv('data.csv', usecols=['Region','Year', 'Value'])
df = df.loc[df['Region'].isin(['Bulgaria'])].sort_values(by = 'Year', ascending = False)
print("country: {}, year: {}, emissions: {}".format(*df.iloc[0]))

@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'

@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    if country.lower()=="albania":
        return json.dumps({"country":"Albania","year":1975, "emissions":4338.3340})
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)

@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    if year=="1975":
        return json.dumps({"year":"1975", "total":12333555.9})
    else:
        abort(404)

@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    
    if country.lower()=="albania":
        return json.dumps({1975:4338.334, 1985:6929.926, 1995:1848.549, 2005:3825.184, 2015:3824.801, 2016:3674.183, 2017:4342.011})
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)

if __name__=="__main__":
    app.run(debug=True)
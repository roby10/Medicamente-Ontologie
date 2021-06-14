#!/usr/bin/env python3

import os
import sys
import re
import time
import pickle
import json

import bs4
import requests


base = 'https://www.anm.ro/nomenclator/medicamente?page='
folder = 'C:/Users/roby/Desktop/master/AWS/data/'

def getcontent(href):
    text = ''
    soup = get_soup_from_link(href)
    #print(soup)
    targets = soup.find_all('div', {'class': re.compile('StandardArticleBody_body')})

    #print(targets)
    if targets:
        for target in targets[0].findChildren(recursive=False):
            if target.name == 'p':
                text += target.text
                #print(target.text)
    return text

def run_full(id):
    link = base + str(id)
    print(link)
    

    try:
        response = requests.get(link)
        soup = bs4.BeautifulSoup(response.content, 'html.parser')
        targets = soup.find_all('div', {'class' : 'table-responsive'})[0].find_all('button')
        #print(len(targets))
    except Exception:
        print('EXCEPTION RAISED. Could not download link : {}. Resuming anyway.'.format(link))
        targets = []


    for target in targets:

        data = {}

        data['Denumire comerciala'] = target.attrs['data-dencom']
        data['DCI'] = target.attrs['data-dci']
        data['Forma farmaceutica'] = target.attrs['data-formafarm']
        data['Concentratia'] = target.attrs['data-conc']
        data['Cod ATC'] = target.attrs['data-codatc']
        data['Actiune terapeutica'] = target.attrs['data-actter']
        data['Prescriptie'] = target.attrs['data-prescript']
        data['Ambalaj'] = target.attrs['data-ambalaj']
        data['Volum ambalaj'] = target.attrs['data-volumamb']
        data['Valabilitate ambalaj'] =  target.attrs['data-valabamb']
        data['Cod CIM'] = target.attrs['data-cim']
        data['Firma / tara producatoare APP'] = target.attrs['data-firmtarp']
        data['Firma / tara detinatoare APP'] = target.attrs['data-firmtard']
        data['Nr. / data ambalaj APP'] = target.attrs['data-nrdtamb']
        #print(target.attrs['data-linkrcp'])
        #print(target.attrs['data-linkpro'])
        #print(target.attrs['data-linkamb'])

        os.mkdir(folder + data['Cod CIM'])
        
        r = requests.get(target.attrs['data-linkrcp'])
        with open(folder + data['Cod CIM'] + '/Rezumat.pdf', 'wb') as f:
            f.write(r.content)


        r = requests.get(target.attrs['data-linkpro'])
        with open(folder + data['Cod CIM'] + '/Prospect.pdf', 'wb') as f:
            f.write(r.content)


        r = requests.get(target.attrs['data-linkamb'])
        with open(folder + data['Cod CIM'] + '/Ambalaj.pdf', 'wb') as f:
            f.write(r.content)

        with open(folder + data['Cod CIM'] + '/Data.json', 'w') as outfile:
            json.dump(data, outfile)





if __name__ == '__main__':
    for i in range(1,10):
        run_full(i)

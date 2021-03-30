import argparse

import sys
import config
import string
import unicodecsv as csv
import urllib
import json
import requests
import ast
from pprint import pprint
from datetime import datetime

def csv_to_file(output):
    with open(config.outputFile, "wb") as outputFile:
        wr = csv.writer(outputFile, quoting=csv.QUOTE_ALL)
        wr.writerows(output)

def display_game_dlc(game_id):
    output = []
    game_endpoint = config.api_endpoint + '/game/'+str(game_id)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    query_params = {'format': 'json','api_key':config.apikey}
    response = requests.get(game_endpoint,params=query_params,headers=headers)

    if response.status_code == 200:
        game_result=response.json()
        if config.showdlc:
            dlc_endpoint= config.api_endpoint + '/dlc/'+str(game_id)
            dlc_data = requests.get(dlc_endpoint,params=query_params,headers=headers)
            dlc_result = dlc_data.json()
            pprint(dlc_result['results'], indent=1)
            #pprint(sorted(dlc_result['results'],key= lambda x: datetime.strptime(dlc_result['results']['release_date'], '%Y-%m-%d %H:%M:%S').date(), reverse=True), indent=1)
        else:
            pprint(game_result['results'], indent=1)
    return response.status_code


def search_games(name):
    output = []
    #set request variables
    base_url = config.search_endpoint


    query_params = {'format': 'json', 'filter': 'name:'+name, 'field_list': 'id,name','sort':'guid:asc','api_key':config.apikey}

    # #create request string
    #request_string = base_url + '&format=json' + '&filter='+query + '&field_list=name'
    #print request_string
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    response = requests.get(base_url,params=query_params,headers=headers)

    if response.status_code == 200:
        json_object=response.json()
        # #get request response
        new_results = json_object['results']
        num_results = json_object['number_of_page_results']
        for result in new_results:
            temp_output = []
            temp_output.append(ast.literal_eval(json.dumps(result['id'])))
            temp_output.append(ast.literal_eval(json.dumps(result['name'])))
            output.append(temp_output)
        if config.outputFile:
            csv_to_file(output)
        else:
            pprint(output, indent=4)
    return response.status_code


def main():
    if config.search:
        search_games(config.search) #ape
    elif config.gid:
        display_game_dlc(config.gid) #3030-9943
    else:
        print "wrong usage need to enter --search or --gid"



if __name__ == '__main__':
  main()

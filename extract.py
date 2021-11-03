import csv
import json

from models import NearEarthObject, CloseApproach
from trying_stuffs import timefunc, memoize
# from workspace.models import NearEarthObject, CloseApproach
# from workspace.trying_stuffs import timefunc, memoize

# @timefunc  # time of completion
@memoize
def load_neos(neo_csv_path='data/neos.csv'):
    """Read near-Earth object information from a CSV file."""
    collection_on_neos = []
    with open(neo_csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            collection_on_neos.append(NearEarthObject(row['pdes'], row['name'], row['diameter'], row['pha']))
    return collection_on_neos

# @timefunc  # time of completion
@memoize
def load_approaches(cad_json_path='data/cad.json'):
    """Read close approach data from a JSON file."""
    with open(cad_json_path) as f:
        data = json.load(f)
    collection_of_approaches = []
    for row in data['data']:
        collection_of_approaches.append(CloseApproach((row[0]), (row[3]), (row[4]), (row[7])))
    return collection_of_approaches

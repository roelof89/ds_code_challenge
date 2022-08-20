# Given that the data won't sync to github (given the size), I made a script to load data
import os
import urllib.request 

file_list = [
    'https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/sr.csv.gz',
    'https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/sr_hex.csv.gz',
    'https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/sr_hex_truncated.csv',
    'https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/city-hex-polygons-8.geojson',
    'https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/city-hex-polygons-8-10.geojson'
]
if not os.path.exists('data/raw'):
    os.makedirs('data/raw')

for f in file_list:
    file_name = 'data/raw/' + f.replace('https://cct-ds-code-challenge-input-data.s3.af-south-1.amazonaws.com/','')
    urllib.request.urlretrieve(f, file_name)

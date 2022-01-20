#!/usr/bin/env python

import os
import kaggle
from shutil import rmtree

import requests

import datetime, json

import argparse
import coloredlogs, logging as log

# global vars
RAW_DATA_PATH = '../../data/raw/'
API_BASE_URL = 'kartik2112/fraud-detection'

"""
def save_json(input_name, data, type='w'):
    with open(RAW_DATA_PATH + input_name, type) as file:
        json.dump(data, file, indent=4, sort_keys=True)
        log.info("%s saved." % input_name)
"""

def checkPath():
    if os.path.exists(RAW_DATA_PATH):
        rmtree(RAW_DATA_PATH, ignore_errors=True)
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    log.info("Path checked.")


def parse_arguments():
    parser = argparse.ArgumentParser(prog="Get data script",
                                     description="Script to get the data about air quality of Lleida using the OpenAQ API service which collects data from air sensors located around the world.")
    parser.add_argument('-p', '--path', dest='path', type=str, default=RAW_DATA_PATH, required=False,
                        help='Custom save data path directory.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, required=False,
                        help='Display monitoring details and create a logging file.')
    return parser.parse_intermixed_args()

def getData():
    kaggle.api.authenticate()
    log.info("Kaggle authenticated.")
    kaggle.api.dataset_download_files(API_BASE_URL, path=RAW_DATA_PATH, unzip=True)
    log.info("Dataset downloaded.")

def main():
   
    global RAW_DATA_PATH
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    args = parse_arguments()

    RAW_DATA_PATH = args.path
    if args.verbose:
        os.makedirs(os.path.dirname(os.path.realpath(__file__)) + "/logs", exist_ok=True)
        file_handler = log.FileHandler('logs\getData_%s.log' % datetime.datetime.now().strftime("%Y-%m-%d")) # year - month - day
        file_handler.setLevel(log.DEBUG)

        formatter = log.Formatter("%(asctime)s %(levelname)s %(message)s")
        file_handler.setFormatter(formatter)
        log.getLogger().addHandler(file_handler)
        
        coloredlogs.install(fmt="%(asctime)s %(levelname)s %(message)s", mode='a', level=log.DEBUG) # mode 'append'

    log.info("Starting...")

    log.info("Checking path...")
    checkPath()

    # Get Data
    log.info("Getting datasets..")
    getData()

    log.info("Completed.\n%s" % ("-"*100 + "\n"))

if __name__ == '__main__':
    main()
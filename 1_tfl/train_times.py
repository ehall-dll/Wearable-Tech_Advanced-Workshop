import requests
import json
import time
from termcolor import colored, cprint

def get_train_times():
    # This is the URL for the API endpoint, we're querying the arrival predictions for Stratford (940GZZLUSTD)
    url = "https://api.tfl.gov.uk/StopPoint/940GZZLUSTD/Arrivals"

    # Send GET request to the API
    response = requests.get(url)

    # Parse the JSON response
    data = json.loads(response.text)

    # Separate the data into two lists, one for each line
    jubilee_trains = sorted([item for item in data if item['lineName'] == 'Jubilee' and item['timeToStation'] <= 600], key=lambda x: x['timeToStation'])
    central_trains = sorted([item for item in data if item['lineName'] == 'Central' and item['timeToStation'] <= 600], key=lambda x: x['timeToStation'])

    # Loop through the data and print each train's arrival time
    cprint("\nUpcoming Jubilee line trains:", 'grey', 'on_white', attrs=['bold'])
    seen_destinations = set()
    for item in jubilee_trains:
        if item['destinationName'] not in seen_destinations:
            if item['timeToStation'] <= 60:
                cprint("A TRAIN IS NOW APPROACHING", 'grey', 'on_yellow', attrs=['blink'])
                cprint("Train to {} expected in {} seconds".format(item['destinationName'], item['timeToStation']), 'grey', 'on_yellow', attrs=['blink'])
            else:
                print("Train to {} expected in {} seconds".format(item['destinationName'], item['timeToStation']))
            seen_destinations.add(item['destinationName'])

    cprint("\nUpcoming Central line trains:", 'red', attrs=['bold'])
    seen_destinations = set()
    for item in central_trains:
        if item['destinationName'] not in seen_destinations:
            if item['timeToStation'] <= 60:
                cprint("A TRAIN IS NOW APPROACHING", 'grey', 'on_yellow', attrs=['blink'])
                cprint("Train to {} expected in {} seconds".format(item['destinationName'], item['timeToStation']), 'grey', 'on_yellow', attrs=['blink'])
            else:
                print("Train to {} expected in {} seconds".format(item['destinationName'], item['timeToStation']))
            seen_destinations.add(item['destinationName'])

# Loop to keep updating the display every 30 seconds
while True:
    get_train_times()
    time.sleep(5)
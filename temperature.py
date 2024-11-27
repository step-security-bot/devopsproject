"""
Returns average temperature of all senseboxes

Parameters:
    boxes (list): List of senseboxes to be queried

Returns:
    avgTemperatur (float): Average temperature of queried sensors
"""

# importing the requests library
import logging
import requests

def avg_temperature(boxes):
    """returns average temperature of {boxes}"""
    total_temperatur = 0

    for boxid in boxes:
        # api-endpoint
        url = "https://api.opensensemap.org/boxes/" + boxid + "?format=json"

        # sending get request and saving the response as response object
        try:
            r = requests.get(url, timeout=10)
        except requests.exceptions.Timeout:
            logging.error("timeout raised")

        # extracting data in json format
        data = r.json()
        temperatur_str = data['sensors'][2]['lastMeasurement']['value']

        # adding current box temperature to total
        total_temperatur+=float(temperatur_str)

    # return average temperature
    return total_temperatur/len(boxes)

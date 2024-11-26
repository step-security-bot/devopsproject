def avgTemperature(boxes):
    # importing the requests library
    import requests
    
    totalTemperatur = 0

    for id in boxes:
        # api-endpoint
        URL = "https://api.opensensemap.org/boxes/" + id + "?format=json"

        # sending get request and saving the response as response object
        r = requests.get(url = URL)

        # extracting data in json format
        data = r.json()
        temperaturStr = data['sensors'][2]['lastMeasurement']['value']

        # adding current box temperature to total
        totalTemperatur+=float(temperaturStr)

    # return average temperature
    return(totalTemperatur/len(boxes))
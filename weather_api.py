import openmeteo_requests
import numpy as np 
from DataFrameHandler import DataFrameHandler

import requests_cache
import pandas as pd
from retry_requests import retry

'''
#class weather_api:

	# Setup the Open-Meteo API client with cache and retry on error
	cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
	retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
	openmeteo = openmeteo_requests.Client(session = retry_session)

	# Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude": 52.52,
		"longitude": 13.41,
		"hourly": ["temperature_2m", "relative_humidity_2m", "weather_code"],
		"timezone": "auto",
		"forecast_days": 15 
	}
	responses = openmeteo.weather_api(url, params=params)

	for i in range ()
	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	print(f"Elevation {response.Elevation()} m asl")
	print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
	hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()

	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature"] = hourly_temperature_2m
	hourly_data["relative_humidity"] = hourly_relative_humidity_2m
	hourly_data["weather_code"] = hourly_weather_code

	hourly_dataframe = pd.DataFrame(data = hourly_data)
	print(hourly_dataframe)

	hd = DataFrameHandler.write_csv(hourly_dataframe)
	print(hd)
'''

'''
data  = DataFrameHandler.read_csv('input/test.csv')
weather_features = pd.DataFrame()
weather_features = DataFrameHandler.write_to_dataframe(weather_features, "Component ID", data['Component ID'])
weather_features = DataFrameHandler.write_to_dataframe(weather_features, "Component Type", data['Component Type'])
weather_features = DataFrameHandler.write_to_dataframe(weather_features, "Deployment Area", data['Deployment Area'])
weather_features = DataFrameHandler.write_to_dataframe(weather_features, "Latitude", data['Revised_Latitude'])
weather_features = DataFrameHandler.write_to_dataframe(weather_features, "Longitude", data['Revised_Longitude'])
weather_features = DataFrameHandler.write_csv(weather_features)
print(weather_features)

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"

params = {
	"latitude": data["Revised_Latitude"],
	"longitude": data["Revised_Longitude"],
	"hourly": ["temperature_2m", "relative_humidity_2m", "weather_code"],
	"timezone": "auto",
	"forecast_days": 1 
	#"forecast_days": 15 
	}
responses = openmeteo.weather_api(url, params=params)

temperature = list()
humidity = list()
weather_code = list()

for i in range (4):
	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[i]

	# Process hourly data. The order of variables needs to be the same as requested.
	hourly = response.Hourly()
	hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
	hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
	hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()
	
	hourly_data = {"date": pd.date_range(
		start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
		end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = hourly.Interval()),
		inclusive = "left"
	)}
	hourly_data["temperature"] = hourly_temperature_2m
	hourly_data["relative_humidity"] = hourly_relative_humidity_2m
	hourly_data["weather_code"] = hourly_weather_code

	temperature.append(np.mean(hourly_data["temperature"]))
	humidity.append(np.mean(hourly_data["relative_humidity"]))
	weather_code.append(hourly_weather_code[0])

DataFrameHandler.write_to_dataframe(data, "temperature", temperature)
DataFrameHandler.write_to_dataframe(data,"Humidity",humidity)
DataFrameHandler.write_to_dataframe(data,"Weather Code", weather_code)
data = DataFrameHandler.write_csv(data)

print(data)
'''
'''
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Define URL for the API request
url = "https://api.open-meteo.com/v1/forecast"

# Define multiple locations (latitude and longitude)
locations = [
    {"row": 0, "latitude": 52.52, "longitude": 13.41},  # Berlin
    {"row": 1, "latitude": 48.8566, "longitude": 2.3522},  # Paris
    {"row": 2, "latitude": 40.7128, "longitude": -74.0060}  # New York
]

# Create a dictionary to store DataFrames for each location
dataframes = {}

# Loop through each location
for location in locations:
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "hourly": "temperature_2m"
    }    
    
    # Make the API request
    responses = openmeteo.weather_api(url, params=params)
    response = responses[location["row"]] # only the first one will have stg 
    
    # Print coordinates, elevation, timezone, and UTC offset from the response
    print(location["row"])
    print(f"Coordinates: {response.Latitude()}°N, {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()} s")
    
    # Process hourly data
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    
    # Prepare the data for a DataFrame
    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ),
        "temperature_2m": hourly_temperature_2m
    }
    
    # Create the DataFrame
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    
    # Store the DataFrame in the dictionary with the location as the key
    dataframes[f"{location['latitude']}_{location['longitude']}"] = hourly_dataframe
    
    # Print the DataFrame
    print(hourly_dataframe)
    
	

# Now `dataframes` contains a DataFrame for each location
'''

import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

#https://weather.codes/australia/

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Define URL for the API request
url = "https://api.open-meteo.com/v1/forecast"

# Define multiple locations (latitude and longitude)
locations = [
    {"id": "ASXX0001", "latitude": 52.52, "longitude": 13.41},  # Berlin
    {"id": "ASXX0089", "latitude": 48.8566, "longitude": 2.3522},  # Paris
    {"id": "ASXX0112", "latitude": 40.7128, "longitude": -74.0060}  # New York
]

# Create a dictionary to store DataFrames for each location
dataframes = {}

# Loop through each location
for location in locations:
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "hourly": ["temperature_2m", "relative_humidity_2m", "weather_code"]
    }    
    
    # Make the API request
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0] 

    # Print coordinates, elevation, timezone, and UTC offset from the response
    print(f"Coordinates: {response.Latitude()}°S, {response.Longitude()}°E")
    location_key = location ["id"]
    print(location_key)
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone: {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()} s")

    # Process hourly data
    hourly = response.Hourly()
    hourly_temperature = hourly.Variables(0).ValuesAsNumpy()
    hourly_humidity = hourly.Variables(1).ValuesAsNumpy()
    hourly_weather_code = hourly.Variables(2).ValuesAsNumpy()

    # Prepare the data for a DataFrame
    hourly_data = {
        "timestamp": pd.date_range(
            start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
            end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=hourly.Interval()),
            inclusive="left"
        ),
        "forecasted_temp": hourly_temperature,
        "forecasted_humidity": hourly_humidity,
        "forecasted_weather_code": hourly_weather_code
    }

    # Create the DataFrame
    weather_time_series = pd.DataFrame(data=hourly_data)

    # Store the DataFrame in the dictionary with the box ID as the key
    dataframes[location_key] = weather_time_series

    # Print the DataFrame
    print(weather_time_series)

    # Save the DataFrame to a CSV file
    output_filename = f"weather_data_{location_key}.csv"
    weather_time_series.to_csv(output_filename, index=False)

    # Print confirmation of saved file
    print(f"DataFrame for {location_key} saved to {output_filename}")

# Save each key of the dataframes dictionary
keys = list(dataframes.keys())
keys_df = pd.DataFrame(keys, columns=['location_key'])
keys_df.to_csv('dataframe_keys.csv', index=False)

print("Keys of the dataframes have been saved to 'dataframe_keys.csv'.")

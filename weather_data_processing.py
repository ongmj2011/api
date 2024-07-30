#from weather_api import weather_api
from DataFrameHandler import DataFrameHandler


# data = weather_api.hd

'''
class weather_data_processing: 

    data = DataFrameHandler.read_csv('input/Test.csv')    

    #visibility
   def visibility_df_processor (df): 
        result = list()
        for i in range (len(df)): 
            result.append(visibility(df.loc[i, 'weather_code']))
        return result

    def visibility (weather_code): 
        if weather_code in {0,1,2}: 
            return "Serene"
        elif weather_code == 3: 
            return "Cloudy"
        elif weather_code in {51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82, 95}:
            return "Rain"
        elif weather_code in {45, 48}: 
            return "Fog"

    visibility_list = visibility_df_processor (data)
    data = DataFrameHandler.write_to_dataframe(data, "Visibility", visibility_list)
    DataFrameHandler.write_csv(data)

    #lightning
    def lightning (weather_code): 
        if weather_code in {95,96,99}: 
            return 1
        else: 
            return 0 
    
    def lightning_df_processor (df): 
        result = list()
        for i in range (len(df)): 
            result.append(lightning(df.loc[i, 'weather_code']))
        return result

    lightning_list = lightning_df_processor(data)
    data = DataFrameHandler.write_to_dataframe (data, "Lightning", lightning_list)

    print(data)
'''


'''visibility'''
data = DataFrameHandler.read_csv('input/in.csv')  

def visibility_df_processor (df): 
    result = list()
    for i in range (len(df)): 
        result.append(visibility(df.loc[i, 'weather_code']))
    return result

def visibility (weather_code): 
    if weather_code in {0,1,2}: 
        return "Serene"
    elif weather_code == 3: 
        return "Cloudy"
    elif weather_code in {51, 53, 55, 56, 57, 61, 63, 65, 66, 67, 80, 81, 82, 95}:
        return "Rain"
    elif weather_code in {45, 48}: 
        return "Fog"

visibility_list = visibility_df_processor (data)
data = DataFrameHandler.write_to_dataframe(data, "Visibility", visibility_list)
DataFrameHandler.write_csv(data)

'''lightning'''
def lightning_df_processor (df): 
    result = list()
    for i in range (len(df)): 
        result.append(lightning(df.loc[i, 'weather_code']))
    return result

def lightning (weather_code): 
    if weather_code in {95,96,99}: 
        return 1
    else: 
        return 0 

lightning_list = lightning_df_processor(data)
data = DataFrameHandler.write_to_dataframe (data, "Lightning", lightning_list)

data = DataFrameHandler.write_csv(data)
print(data)

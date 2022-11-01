import requests
import random # only used to generate example data

# credentials for belfast.pvos.org (for this particular sensor feed)
public_key = "4wzyjqhq63t5"
private_key = "pe2y29qanm3n"

# these will stay fixed:
base_url = "http://belfast.pvos.org/data/"
full_url = base_url+public_key

# example data:
distance = random.randint(10,20)
temp_1=11.25
temp_2=57.4

# the JSON object we'll be POST-ing to 'full_url' ...
# NOTE: we must include the private_key as one of the parameters;
# and 'distance_meters' is one of several possible parameters in the postgres database.
myobj = {"private_key":private_key, "temperature_c_1":temp_1,"temperature_c_2":temp_2}

x = requests.post(full_url, data = myobj)
print(myobj) 
print(x.text)

